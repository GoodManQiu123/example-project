<script setup>
// define the props passed from the parent component
defineProps({
  author: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <!-- popover component to display the author information -->
  <VaPopover class="mr-2 mb-2">
    <!-- popover icon -->
    <template #icon>
      <VaIcon name="account_circle" size="large"/>
    </template>
    <!-- popover content -->
    <template #title>
      <p class="mb-1">{{ author?.name }}</p>
    </template>
    <!-- popover body -->
    <template #body>
      <!-- display the author email and affiliation if available -->
      <div v-if="author.email" class=" flex items-center justify-start text-sm">
        <VaIcon class="mr-1" name="mail" size="small"/>
        {{ author.email }}
      </div>
      <div v-if="author.affiliation" class="flex items-center justify-start text-sm">
        <VaIcon class="mr-1" name="apartment" size="small"/>
        {{ author.affiliation }}
      </div>
    </template>
    <!-- chip to display the author name and the target that trigger popover -->
    <VaChip class="mr-1 leading-none" icon="person" size="small" square outline>
      {{ author?.name }}
    </VaChip>
  </VaPopover>
</template>

