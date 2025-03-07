<script setup>
import { nextTick, ref } from "vue";
import DashboardCard from "@/components/DashboardCard.vue";
import UserChip from "@/components/UserChip.vue";
import req from "@/utils/req.js";
// import dashboardExample from '@/lib/exampleDashboard.json';

const uploaded = ref(false);
const ready = ref({
  sameTopic: -1,
  topicConnections: -1,
  coAuthors: -1,
  affiliations: -1,
  citedTree: -1,
  citedByTree: -1,
});
const paper = ref({});
const filename = ref(null);
const cardRef = ref();

const onFileAdded = async (file) => {
  if (file?.length === 1) {
    uploaded.value = true;
    paper.value = {};
    ready.value = {
      sameTopic: 0,
      topicConnections: 0,
      coAuthors: 0,
      affiliations: 0,
      citedTree: 0,
      citedByTree: 0,
    };
    filename.value = file[0].name;
    const data = new FormData();
    data.append('file', file[0]);
    ready.value = {
      sameTopic: 0,
      topicConnections: 0,
      coAuthors: 0,
      affiliations: 0,
      citedTree: 0,
      citedByTree: 0,
    };
    let res = await req.post('/analysis/upload', data);
    res = res.data.data;
    // await new Promise((resolve) => setTimeout(resolve, 3000));
    // const res = dashboardExample.data;
    console.log('analyzed result', res);
    paper.value = {
      articleId: res.articleId,
      title: res.metadata?.title,
      authors: res.authors,
      doi: res.metadata?.doi,
      date: res.metadata?.published_date,
      journal: res.metadata?.journal,
      publisher: res.metadata?.publisher,
      abstract: res.content?.abstract,
      keywords: res.content?.keywords,
      references: res.references,
    };
    console.log('paper', paper.value);
    ready.value = {
      sameTopic: paper.value.keywords?.length > 0 ? 1 : -1,
      topicConnections: paper.value.keywords?.length > 0 ? 1 : -1,
      coAuthors: paper.value.authors?.length > 0 ? 1 : -1,
      affiliations: -1,
      citedTree: paper.value.references > 0 ? 1 : -1,
      citedByTree: paper.value.references > 0 ? 1 : -1,
    };
    await nextTick();
    if (cardRef.value) {
      cardRef.value.scrollIntoView({ behavior: 'smooth' });
    }
  }
};
</script>

<template>
  <div class="p-4">
    <VaFileUpload
        type="single"
        file-types="application/msword, application/pdf"
        @file-added="onFileAdded"
    >
      <div class="p-4 border-2 border-gray-300 border-dashed">
        <div class="upload">
          <VaIcon class="mr-2" size="large" name="upload" color="primary" />
          <p>
            <span>Click</span>or<span>Drag & Drop</span>a file to upload
          </p>
        </div>
      </div>
    </VaFileUpload>
    <VaAlert
        v-if="filename"
        color="success"
        outline
    >
      <template #icon>
        <VaIcon name="attach_file" color="success" />
      </template>
      {{ filename }}
    </VaAlert>
    <div class="pt-4" ref="cardRef">
      <VaCard
          v-if="Object.keys(paper).length > 0"
          class="min-h-32 relative mb-4"
      >
        <VaCardTitle>
          <span v-if="paper?.title" class="ml-3 font-black text-lg">
            {{ paper.title }}
          </span>
          <span v-else class="ml-3 font-black text-lg">- No Title Found -</span>
        </VaCardTitle>
        <VaCardContent class="paper break-words overflow-hidden -mt-2">
          <table class="va-table">
            <tbody>
            <tr v-if="paper?.authors">
              <td>AUTHOR</td>
              <td>
                <UserChip
                    v-for="author in paper.authors"
                    :key="author.id"
                    :author="author"
                />
              </td>
            </tr>
            <tr v-if="paper?.doi">
              <td>DOI</td>
              <td>
                <VaIcon class="mr-2" size="small" name="share" />
                <a class="text-primary" :href="'https://doi.org/' + paper.doi" target="_blank">{{ paper.doi }}</a>
              </td>
            </tr>
            <tr v-if="paper?.date">
              <td>DATE</td>
              <td>{{ paper.date }}</td>
            </tr>
            <tr v-if="paper?.journal">
              <td>JOURNAL</td>
              <td>{{ paper.journal }}</td>
            </tr>
            <tr v-if="paper?.publisher">
              <td>PUBLISHER</td>
              <td>{{ paper.publisher }}</td>
            </tr>
            <tr v-if="paper?.abstract">
              <td>ABSTRACT</td>
              <td>{{ paper.abstract }}</td>
            </tr>
            <tr v-if="paper?.keywords">
              <td>KEYWORDS</td>
              <td>
                <VaChip
                    v-for="(keyword, index) in paper.keywords"
                    :key="index"
                    class="mr-1 leading-none"
                    size="small"
                    square
                >
                  {{ keyword }}
                </VaChip>
              </td>
            </tr>
            <tr v-if="paper?.references">
              <td>REFERENCES</td>
              <td>{{ paper.references }}</td>
            </tr>
            </tbody>
          </table>
        </VaCardContent>
      </VaCard>
    </div>
    <div class="grid grid-cols-6 gap-4">
      <div class="card-section">TOPIC</div>
      <DashboardCard
          class="col-span-3"
          :ready="ready.sameTopic"
          section="Topic"
          title="Same Topic"
          content="Explore the papers with same topics"
          link="/topic/same-topic"
          :paper-id="paper?.articleId"
      />
      <DashboardCard
          class="col-span-3"
          :ready="ready.topicConnections"
          section="Topic"
          title="Topic Connections"
          content="Explore the connections between topics"
          link="/topic/connections"
          :paper-id="paper?.articleId"
      />
      <div class="card-section">AUTHOR</div>
      <DashboardCard
          class="col-span-3"
          :ready="ready.coAuthors"
          section="Author"
          title="Co-Authors"
          content="Explore the co-authors of the paper"
          link="/author/co-authors"
          :paper-id="paper?.articleId"
      />
      <DashboardCard
          class="col-span-3"
          :ready="ready.affiliations"
          section="Author"
          title="Affiliations"
          content="Explore the affiliations of the authors of the paper"
          link="/author/affiliations"
          :paper-id="paper?.articleId"
      />
      <div class="card-section">REFERENCE</div>
      <DashboardCard
          class="col-span-3"
          :ready="ready.citedTree"
          section="Reference"
          title="Cited Tree"
          content="Explore the papers that are cited by the paper"
          link="/reference/cited"
          :paper-id="paper?.articleId"
      />
      <DashboardCard
          class="col-span-3"
          :ready="ready.citedByTree"
          section="Reference"
          title="Cited-By Tree"
          content="Explore the papers that cite the paper"
          link="/reference/cited-by"
          :paper-id="paper?.articleId"
      />
    </div>
  </div>
</template>

<style scoped>
.upload {
  @apply h-32 flex justify-center items-center mb-2 text-center;
}
.upload span {
  @apply text-lg font-black mx-2;
}
.paper div {
  @apply mb-2;
}
.paper span:nth-child(odd) {
  @apply font-bold mr-2;
}
.va-table tr {
  @apply border-b-2 border-gray-300;
}
.va-table td {
  vertical-align: baseline!important;
  @apply py-1 text-justify;
}
.va-table td:first-child {
  @apply font-bold text-end;
}
.va-table td:last-child {
  @apply leading-relaxed;
}
.card-section {
  @apply font-black text-2xl col-span-6 border-l-4 border-solid pl-4 border-gray-300;
}
</style>
