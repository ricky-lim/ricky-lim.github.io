<template>
  <v-container>
    <p class="dropcase">
      Hello, my name is Ricky Lim.
    </p>
    <p>
      I love building data analytics tools to do R&D research and business questions.
    </p>
  </v-container>
</template>
<style>
.dropcase:first-letter {
  initial-letter: 2;
  float: left;
  font-size: 75px;
  line-height: 60px;
  padding-top: 4px;
  padding-right: 8px;
  padding-left: 3px;
}
</style>
<script>
export default {
  name: 'About',
}
</script>
