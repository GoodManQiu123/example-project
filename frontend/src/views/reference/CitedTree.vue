<script setup>
import { ref } from 'vue';
import { useRoute } from "vue-router";
import { DataSet, Network } from 'vis-network/standalone';
import Net from "@/layouts/NetLayout.vue";
import SearchResult from "@/components/SearchResult.vue";
import { authors2Str, generateOptions } from "@/utils/network.js";
import PaperList from "@/components/PaperList.vue";
import req from "@/utils/req.js";

const search = ref(''); // search input value
const resultModal = ref(false); // search result modal state
const searchResults = ref(null); // search results

const netResults = ref(null); // network data
const networkContainer = ref(null); // network container
let nodes = new DataSet([]); // network nodes
let edges = new DataSet([]); // network edges
let network = null; // network instance
const originalPaper = ref({}); // original paper
const selectedNodeId = ref(null); // selected node id

const searchLoading = ref(false); // search loading state
const generateLoading = ref(false); // generate network loading state

// method to handle the search action
const handleSearch = async () => {
  if (search.value !== '') {
    searchLoading.value = true; // start search button loading
    const data = await req.get('/catalog/papers/search', { title: search.value }); // request data from the server
    console.log('Cited Tree: Searched Results', data.data)
    searchResults.value = data.data.data;
    resultModal.value = true;
    searchLoading.value = false;
  }
};

const handleResultSelect = async (id) => {
  console.log('Cited Tree: Selected Paper ID', id);
  originalPaper.value.articleId = id;
  netResults.value = null; // clear the previous network data
  resultModal.value = false; // close the search result modal
  generateLoading.value = true; // start generating network loading
  nodes.clear(); // clear the nodes
  edges.clear(); // clear the edges
  let data = await req.get('/catalog/cited-tree', { article_id: id }); // request data from the server
  data = data.data.data;
  console.log('Cited Tree: Network Data', data);
  originalPaper.value = data.papers.find(paper =>
      paper.articleId === originalPaper.value.articleId); // get the original paper
  netResults.value = data; // set the network data
  search.value = ''; // clear the search input
  initializeNetwork();
  generateLoading.value = false; // stop generating network loading
};

// check if the paperId is in the query, if so, generate the network
const route = useRoute();
if (route.query.paperId) {
  handleResultSelect(+route.query.paperId);
}

// initialize the network
const initializeNetwork = () => {
  if (networkContainer.value) {
    // convert papers to nodes
    const paperNodes = netResults.value.papers.map(paper => ({
      id: paper.articleId,
      title: `${paper.title}${authors2Str(paper.authors)}`,
      label: paper.authors[0]?.name,
      color: paper.articleId === originalPaper.value.articleId ? '#FFC107' : null, // highlight the original paper
    }));

    // convert connections to edges
    const edgesArray = netResults.value.connections.flatMap(connection =>
        connection?.toPaper?.map(toId => ({
          from: connection.fromPaper,
          to: toId,
        }))
    );

    // create DataSet instances for nodes and edges
    nodes = new DataSet(paperNodes);
    edges = new DataSet(edgesArray);

    // define the data and options for the network
    const data = { nodes, edges };
    const options = generateOptions({
      layout: {
        hierarchical: { // hierarchical layout
          enabled: false,
          direction: 'UD', // from up to down
          sortMethod: 'directed', // or 'hubsize'
        }
      },
      edges: {
        arrows: {
          to: { enabled: true, scaleFactor: 1, type: 'arrow' }, // configure arrow size and style
        },
      },
    });

    // initialize the network
    network = new Network(networkContainer.value, data, options);

    // event listener for node selection
    network.on("selectNode", params => {
      if (params.nodes.length > 0) {
        const selectedNodeId = params.nodes[0];
        console.log('selectedNodeId', selectedNodeId)
        highlightListItem(selectedNodeId); // function to highlight the list item corresponding to the selected node
      }
    });

    // event listener for node deselection
    network.on("deselectNode", () => {
      selectedNodeId.value = null; // clear selected node ID when a node is deselected
    });
  }
};

// method to highlight the list item
const highlightListItem = (nodeId) => {
  selectedNodeId.value = nodeId;
};

// method to highlight the node and the list item at the same time
const highlightNode = (nodeId) => {
  if (network && nodeId) {
    // select the node and highlight the edges
    network.selectNodes([nodeId], true);
    // highlight the list item
    highlightListItem(nodeId);
  }
};
</script>

<template>
  <!-- search result modal -->
  <SearchResult
      v-model="resultModal"
      :search="search"
      :searchResults="searchResults"
      @select="handleResultSelect"
  />
  <!-- network layout -->
  <Net>
    <template #list>
      <div class="p-4 sticky top-0 shadow bg-white/20 backdrop-blur z-10">
        <!-- search input -->
        <VaInput
            v-model="search"
            class="w-full"
            label="search for a paper"
            @keyup.enter="handleSearch"
        >
          <template #append>
            <VaButton
                class="ml-2 bg-primary-500 text-white"
                :disabled="!search"
                icon="search"
                :loading="searchLoading"
                @click="handleSearch"
            />
          </template>
        </VaInput>
      </div>
      <!-- list of papers -->
      <PaperList
          v-if="netResults"
          :originalPaper="originalPaper"
          :papers="netResults.papers"
          :selectedNodeId="selectedNodeId"
          @highlightNode="highlightNode"
      />
      <p v-else v-show="!generateLoading" class="mt-4 text-center text-gray-500 uppercase">
        * Search for a paper first *
      </p>
      <!-- loading state -->
      <div v-if="generateLoading" class="w-full text-center">
        <VaProgressCircle
            class="mx-auto mt-8 mb-2"
            :thickness="0.6"
            indeterminate
        />
        <p class="text-gray-500">Generating ...</p>
      </div>
    </template>
    <!-- network graph -->
    <template #graph>
      <div ref="networkContainer" class="mx-auto w-full h-full"></div>
    </template>
  </Net>
</template>
