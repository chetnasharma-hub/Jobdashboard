

<template>
  <div class="container mt-4">
 <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  Add new Job
</button>

<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Add new Job</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
           <div class="card p-4">
    <input class="form-control " placeholder="Title" v-model="job.title">
    <select class="form-control mb-2" v-model="job.status">
        <option value="draft">Draft</option>
        <option value="requested">Requested</option>
        <option value="posted">Posted</option>
        <option value="filled">Filled</option>
      </select>
    <select class="form-control mb-2" v-model="job.category">
        <option value="full_time">Full Time</option>
        <option value="part_time">Part Time</option>
        <option value="Internship">Internship</option>
        <option value="volunteer">Volunteer</option>
      </select>
            <input class="form-control mb-2" placeholder="Address" v-model="job.address">
      <input class="form-control mb-2" placeholder="City" v-model="job.city">
      <input class="form-control mb-2" placeholder="State" v-model="job.state">

      <input type="date" class="form-control mb-2" v-model="job.start_date">
      <input type="date" class="form-control mb-2" v-model="job.end_date">

      <textarea class="form-control mb-2" placeholder="Description" v-model="job.description"></textarea>

      <input type="file" class="form-control mb-3" @change="handleFile">
       <button type="button" class="btn btn-primary" @click="add_job">
        Add Job
      </button>
    </div>
      </div>

    </div>
  </div>
</div>
 
    
  </div>
</template>

<script>
import axios from 'axios';

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
export default {
    name: 'AddingJob',
  data(){
    return {
    job:{
    title:"",
    status:"draft",
    category:"full_time",
    address:"",
    city:"",
    state:"",
    start_date:"",
    end_date:"",
    description:"",
    job_profile_pic:null
  },
  selectedFile:null
    };
  },

  methods:{
      handleFile(event){
      this.selectedFile=event.target.files[0]

    },
    async add_job(){
      console.log(this.job)
      const formData = new FormData()
      
      formData.append("title",this.job.title);
      formData.append("status",this.job.status);
      formData.append("category",this.job.category);
      formData.append("city",this.job.city);
      formData.append("state",this.job.state);
      formData.append("start_date",this.job.start_date);
      formData.append("end_date",this.job.end_date);
      formData.append("description",this.job.description);
      formData.append("job_profile_pic", this.selectedFile);

      axios.post('http://localhost:8000/api/jobs/', formData,{
        headers:{ "Content-Type": "multipart/form-data" }
      })

      .then (res =>{
        console.log(res)
      })
  
    },
  }
 


};
</script>
