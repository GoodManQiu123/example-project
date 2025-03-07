<script setup>

</script>

<template>
  <div class="text-center text-xl pt-8">
    Coming soon ...
    <!--<VaList v-if="netResults" class="p-2">-->
    <!--  <VaListItem-->
    <!--      :class="{'highlight': selectedNodeId === originalPaper.articleId}"-->
    <!--      class="p-2 cursor-pointer bg-blue-50 hover:bg-gray-100 border-b border-gray-200 border-solid"-->
    <!--      @click="highlightNode(originalPaper.articleId)"-->
    <!--  >-->
    <!--    <VaListItemSection>-->
    <!--      <p class="ml-1 mb-1 text-sm text-blue-600 font-bold">Origin Paper</p>-->
    <!--      <VaListItemLabel class="mb-1">-->
    <!--        <span class="ml-1">{{ originalPaper.title }}</span>-->
    <!--      </VaListItemLabel>-->
    <!--      <VaListItemLabel v-if="originalPaper?.authors.length > 0" caption>-->
    <!--        <UserChip-->
    <!--            v-for="author in originalPaper?.authors"-->
    <!--            :key="author.id"-->
    <!--            :author="author"-->
    <!--        />-->
    <!--      </VaListItemLabel>-->
    <!--    </VaListItemSection>-->
    <!--  </VaListItem>-->
    <!--  <template v-for="paper in netResults.papers" :key="paper.id">-->
    <!--    <VaListItem-->
    <!--        v-if="paper.articleId !== originalPaper.articleId"-->
    <!--        :class="{'highlight': paper.articleId === selectedNodeId}"-->
    <!--        class="p-2 cursor-pointer hover:bg-gray-100 border-b border-gray-200 border-solid"-->
    <!--        @click="highlightNode(paper.articleId)"-->
    <!--    >-->
    <!--      <VaListItemSection>-->
    <!--        <VaListItemLabel class="mb-1">-->
    <!--          <span class="ml-1">{{ paper.title }}</span>-->
    <!--        </VaListItemLabel>-->
    <!--        <VaListItemLabel v-if="paper.authors.length > 0" caption>-->
    <!--          <UserChip-->
    <!--              v-for="author in paper.authors"-->
    <!--              :key="author.id"-->
    <!--              :author="author"-->
    <!--          />-->
    <!--        </VaListItemLabel>-->
    <!--      </VaListItemSection>-->
    <!--    </VaListItem>-->
    <!--  </template>-->
    <!--</VaList>-->
  </div>
</template>

<style scoped>

</style>
