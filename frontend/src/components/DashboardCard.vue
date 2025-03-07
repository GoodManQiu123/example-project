<script setup>
import { useRouter } from "vue-router";

// create a router instance for routing
const router = useRouter();

// define props of the component that will be passed from the parent component
const props = defineProps({
  ready: Number,
  title: String,
  section: String,
  content: String,
  link: String,
  paperId: Number,
})

// method for getting the icon based on the ready prop
const getReadyIcon = () => {
  switch (props.ready) {
    case -1:
      return 'block';
    case 0:
      return 'loop';
    case 1:
      return 'check';
  }
}

// method for getting the stripe color based on the ready prop
const getReadyStripe = () => {
  switch (props.ready) {
    case -1:
      return 'danger';
    case 0:
      return 'info';
    case 1:
      return 'success';
  }
}

// method for handling the click event on the card
const handleClick = (link) => {
  if (link) {
    // if paperId is present, pass it as a query parameter for page default actions
    return props.paperId ? router.push({ path: link, query: { paperId: props.paperId } }) : router.push(link);
  }
}

</script>

<template>
  <VaCard
      class="flex flex-row min-h-44 min-w-72 cursor-pointer relative"
      :stripe="ready !== 0"
      :stripe-color="getReadyStripe()"
      @click="handleClick(link)"
  >
    <!--stripe section-->
    <VaProgressBar v-if="ready === 0" class="absolute top-0" :size="5" indeterminate />
    <!--card content-->
    <div class="flex items-center h-full">
      <div class="flex-1">
        <!--card title-->
        <VaCardTitle>
          <div>
            <p class="font-black text-lg">{{ title }}</p>
            <p class="text-gray-400">{{ section }}</p>
          </div>
        </VaCardTitle>
        <!--card content-->
        <VaCardContent class="break-words overflow-hidden h-full leading-normal">
          <p class="text-gray-500">{{ content }}</p>
        </VaCardContent>
      </div>
      <!--card icon-->
      <div class="w-auto items-center justify-end text-end pr-4">
        <VaIcon class="icon" size="4rem" :name="getReadyIcon()" />
      </div>
    </div>
  </VaCard>
</template>

<style scoped>
.icon {
  width: 4rem;
}
</style>
