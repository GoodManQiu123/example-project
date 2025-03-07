<script setup>
import UserChip from "@/components/UserChip.vue";

// define the props passed from the parent component
defineProps({
  modelValue: Boolean,
  search: String,
  searchResults: Array
});

// define the emits to pass the events to the parent component
const emit = defineEmits(['update:modelValue', 'select']);

// method to emit the event to update the model value
const updateModelValue = (value) => {
  emit('update:modelValue', value);
};

// method to emit the event to select the result
const selectResult = (id) => {
  emit('select', id);
  updateModelValue(false); // close modal
};

// method to close the modal
const handleClose = () => {
  updateModelValue(false);
};
</script>

<template>
  <VaModal
      :model-value="modelValue"
      class="my-0 border-solid border"
      max-height="600px"
      hide-default-actions
      fixed-layout
      blur
      @update:model-value="updateModelValue"
  >
    <VaList>
      <!-- label(title) for the search results -->
      <VaListLabel class="sticky top-0 pb-4 bg-white/90 z-10">
        <span v-if="searchResults.length === 0" class="font-bold">No</span>
        Results for <span class="ml-1 font-bold text-xl">{{ search }}</span>
      </VaListLabel>
      <!-- list of search results -->
      <VaListItem
          v-for="result in searchResults"
          :key="result.articleId"
          class="p-2 my-1 cursor-pointer hover:bg-gray-100 border-b border-gray-200 border-solid"
          @click="selectResult(result.articleId)"
      >
        <VaListItemSection>
          <VaListItemLabel class="mb-3">
            <span class="ml-1">{{ result.title }}</span>
          </VaListItemLabel>
          <VaListItemLabel v-if="result.authors.length > 0" caption>
            <UserChip
                v-for="author in result.authors"
                :key="author.authorId"
                :author="author"
            />
          </VaListItemLabel>
        </VaListItemSection>
      </VaListItem>
    </VaList>
    <!-- footer for the modal with close button -->
    <template #footer>
      <VaButton @click="handleClose"> Close </VaButton>
    </template>
  </VaModal>
</template>
