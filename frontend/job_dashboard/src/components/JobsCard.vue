<template>
<div class="container mt-4">
    <h1 class="mb-4">Jobs</h1>

    <div class="row g-4" >
        <div v-if="list.length === 0" class="col-12">
          <h1 class="text-center">No jobs available</h1>
        </div>
        <div class="col-md-4" v-for="item in list" :key="item.id">
            <div class="card ">
                <img class="card-img-top" :src="item.job_profile_pic" alt="Job Image" style="height: 200px;">
                <div class="card-body">
                    <h5 class="card-title">{{ item.title }}</h5>
                    <p class="card-text">{{ item.description }}</p>
                    <div class="job-meta-icons">
                       <span>📌 {{ item.status }}</span>
                       <span>🏙 {{ item.city }}</span>
                       <span>📍 {{ item.state }}</span>
                      </div>


                    <div class="card">
                    <button type="button" class="btn btn-primary mb-2" data-bs-toggle="modal" data-bs-target="#exampleModal2"  @click="openEdit(item.id)">
                        Edit
                    </button>
                <button type="button" class="btn btn-danger" @click="delete_job(item.id)">
                   Delete Button
                </button>   
                <button type="button" class="btn btn-secondary mt-2" @click="duplicate_job(item.id)">
                  Duplicate
                </button>

                    </div>
                </div>  
            </div>
        </div>    
    </div>    
    <div class="modal fade" id="exampleModal2" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Add new Job</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
        <div class="modal-body">
 
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
                <label for="start_date">Start Date</label>
                <input type="date" class="form-control mb-2" v-model="job.start_date" id="start_date">
                <label for="end_date">End Date</label>
                <input type="date" class="form-control mb-2" v-model="job.end_date" id="end_date">
                <textarea class="form-control mb-2" placeholder="Description" v-model="job.description"></textarea>
                <label for="profile">Display Picture</label>
                <input type="file" id="profile" class="form-control mb-3" @change="onFileselected">
                <button type="button" class="btn btn-primary" @click="save_job">
                    Save
                </button>
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
    name: 'JobsCard',
  data(){
    return {
    list : [],
    selectedId: null, 
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
    }
  },
 methods: {
  async openEdit(id) {
 
    const response = await axios.get(`http://localhost:8000/api/jobs/${id}/`);

    this.job = response.data;   
    console.log(' job_id:', response.data);
  }, 
async save_job() {
  try {
    const formData = new FormData()

    formData.append("title", this.job.title)
    formData.append("status", this.job.status)
    formData.append("category", this.job.category)
    formData.append("address", this.job.address)
    formData.append("city", this.job.city)
    formData.append("state", this.job.state)
    formData.append("start_date", this.job.start_date)
    formData.append("end_date", this.job.end_date)
    formData.append("description", this.job.description)

    if (this.selectedFile) {
      formData.append("job_profile_pic", this.selectedFile)
    }

    await axios.put(
      `http://localhost:8000/api/jobs/${this.job.id}/`,
      formData,
      { headers: { "Content-Type": "multipart/form-data" } }
    )

    alert("Job saved successfully")
        
    const res = await axios.get("http://localhost:8000/api/jobs/")
    this.list = res.data


  } catch (error) {
    if (error.response && error.response.status === 400) {
      const backendError = error.response.data

   
      if (backendError.non_field_errors) {
        alert(backendError.non_field_errors[0])
      } else {
        alert("Validation error")
      }
    } else {
      alert("Server error")
    }
  }
},
async duplicate_job(id) {
  try {
    await axios.post(
      `http://localhost:8000/jobs/${id}/duplicate/`
    )

    alert("Job duplicated successfully")


    const res = await axios.get("http://localhost:8000/api/jobs/")
    this.list = res.data

  } catch (error) {
    console.log(error.response?.data)
    alert("Failed to duplicate job")
  }
},
  async delete_job(id){
        const response = await axios.delete(
      `http://localhost:8000/api/jobs/${id}/`
    );
    console.log(response)
    
    alert("Job deleted successfully")
    
    const res = await axios.get("http://localhost:8000/api/jobs/")
    this.list = res.data

  }
},
    async mounted() {
    const response = await axios.get('http://localhost:8000/api/jobs/');
    console.log(response.data); 
    this.list = response.data;
  },
};
</script>

<style>
  .job-meta-icons {
  display: flex;
  gap: 12px;
  font-size: 13px;
  color: #444;
  margin-top: 8px;
  margin-bottom: 8px;  
}

</style>