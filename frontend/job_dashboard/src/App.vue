<template>
  <div class="container mt-3">
    <div class="d-flex justify-content-start mb-3">
      <AddingJob />
    </div>
    <JobsCard />

  </div>
</template>

<script>
  import JobsCard from './components/JobsCard.vue';
  import AddingJob from './components/AddingJob.vue';
  export default{
    name:'App',
    components:{
      JobsCard,
      AddingJob

    }
  }
</script>