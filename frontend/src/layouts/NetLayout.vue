<template>
  <!-- basic layout of each graph related page -->
  <div class="flex gap-2 h-full">
    <div class="w-1/3 min-w-[300px] flex-none shadow-xl overflow-auto">
      <!-- slot for the list of papers -->
      <slot name="list"></slot>
    </div>
    <div class="flex-auto">
      <!-- slot for the graph -->
      <slot name="graph"></slot>
    </div>
  </div>
</template>
