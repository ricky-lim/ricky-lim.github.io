<template>
  <v-container>
    <v-row>
      <v-col>
        <div class="text-h2 text-md-h1 text-center">
          Welcome!
        </div>
      </v-col>
    </v-row>
    <v-row>
      <year-progress/>
    </v-row>

  </v-container>
</template>

<script>
import YearProgress from "@/components/YearProgress";

export default {
  name: 'Home',
  components: {YearProgress},
  data: () => ({}),
}
</script>
