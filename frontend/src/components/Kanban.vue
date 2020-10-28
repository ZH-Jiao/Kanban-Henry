<template>
<div class="b-container mt-5 mx-5">

    
      <FormulateForm v-model="formValues" @submit="handleSubmit">
        <FormulateInput name="name" label="Name" validation="required" />
        <FormulateInput name="education" label="Education" validation="required" />
        <FormulateInput name="contact" label="Contact" validation="required|number" />
        <FormulateInput type="submit" label="Add Applicant"/>
      </FormulateForm>
    
    <br>
    <b-button block pill v-b-toggle.collapse-1 variant="outline-primary" class="">Switch Between Abstract / Detail View</b-button>
    <div class="row mt-4">
      <div class="col-4" v-for="bName in boardName" :key="bName">
        <div class="p-2 alert alert-success">
          <h3>{{bName}}</h3>
          <!-- Backlog draggable component. Pass arrBackLog to list prop -->
          <draggable
            class="list-group kanban-column"
            :list="listBoard[bName]"
            group="tasks"
            @end="updateStatus"
          >
            <div
              class="list-group-item"
              v-for="element in listBoard[bName]"
              :key="element.name"
            >
              <div>
              <!-- {{ element.name }} -->
              <!-- Basic Info -->
              <div v-html="element.renderCard()"></div>

              <!-- Collaps Detail -->
              
              <b-collapse id="collapse-1" class="mt-2">
                <b-card>
                  <!-- Rate -->
                  <!-- Add Comment -->
                  <FormulateForm v-model="reviewForm" @submit="submitReview(element)">
                    <FormulateInput
                      name="rate"
                      :options="{1: 1, 2: 2, 3: 3, 4: 4, 5:5}"
                      type="select"
                      placeholder="Your rating"
                      label="How well is this applicant?"
                    />
                    <FormulateInput name="author" placeholder="Reviewer" validation="required" />
                    <FormulateInput name="comment" placeholder="Enter your comment" validation="required" />

                  <!-- <FormulateInput class="col" name="rate" placeholder="Enter your rate" validation="required" /> -->
                  <FormulateInput type="submit" :disabled="element.reviewed" label="Submit" />
                  <p v-show="element.reviewed">Submitted! Refresh the page to see updated result</p>
                  </FormulateForm>
                </b-card>
                <b-card>
                  <p>Comments</p>
                  <b-list-group>
                    <b-list-group-item class="d-flex align-items-center" v-for="comment in element.comments" v-bind:key="comment.author">
                      <b-avatar class="mr-3"></b-avatar>
                      <span class="mr-auto">{{comment['author']}}</span>
                      <span class="mr-auto">{{comment['content']}}</span>
                    </b-list-group-item>
                  </b-list-group>
                   
                  
                </b-card>
              </b-collapse>
              </div>

            </div>
          </draggable>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable"
import axios from 'axios'

const BASE_URL = "http://localhost:8000/"

export default {
  name: 'Kanban',
  components: {
    draggable,

  },
  data() {
    return {
      formValues: {},
      newApplicant: "",
      boardName: [
        'Applied',
        'PhoneScreen',
        'OnSite',
        'Offered',
        'Accepted',
        'Rejected'
      ],
      listBoard: {
          'Applied': [],
          'PhoneScreen': [],
          'OnSite': [],
          'Offered': [],
          'Accepted': [],
          'Rejected': []
      },
      tempRate: 0,
      reviewForm: null,
    }
  },
  mounted: function() {
    console.log(this.listBoard)
    this.getAllApplicants();
    console.log(this.listBoard)
  },
  methods: {
    handleSubmit() {
      console.log(this.formValues);
      var card = new Card(
        this.formValues['name'],
        this.formValues['education'],
        this.formValues['contact']
      );
      this.listBoard['Applied'].push(card);
      console.log(this.listBoard['Applied']);

      axios({
        url: BASE_URL + "add-applicant",
        method: 'post',
        headers: { 
          'Accept': 'application/json',
          'Content-Type': 'application/json' },
        data: {
          name: card.name,
          education: card.education,
          contact: card.contact,
          status: 'Applied',
          rate: 0,
          rate_number: 0
        }
      });
      
    },

    submitReview(card) {
      console.log("fired " + this.reviewForm);
        axios({
        url: BASE_URL + "add-rate",
        method: 'post',
        headers: { 
          'Accept': 'application/json',
          'Content-Type': 'application/json' },
        data: {
          'contact': card.contact,
          'newRate': this.reviewForm['rate']
        }
      });
      
      // submit comment
      
        axios({
        url: BASE_URL + "add-comment",
        method: 'post',
        headers: { 
          'Accept': 'application/json',
          'Content-Type': 'application/json' },
        data: {
          'contact': card.contact,
          'author': this.reviewForm['author'],
          'content': this.reviewForm['comment']
        }
      });
      card.reviewed = true;
      
    },

    getAllApplicants() {
      // this.refreshList();
      var entry = null;
      axios({
        url: BASE_URL + "get-all-applicants",
        method: 'get',
        headers: { 
          'Accept': 'application/json',
          'Content-Type': 'application/json' },
      })
      .then(response => {
        console.log(response.data[0]);
        for (entry of response.data) {
          var card = new Card(entry.name, entry.education, entry.contact);
          card.rate = entry.rate;
          card.comments = entry.comment;
          this.listBoard[entry.status].push(card)
        }
      })
    },

    refreshList() {
      var n = null;
      for (n of this.boardName) {
        this.listBoard[n] = []
      }
    },

    updateStatus() {
      console.log("updating status");
      for (var i = 0; i < this.boardName.length; i++) {
        var cur_board = this.boardName[i];
        var board = this.listBoard[cur_board];
        for (var j = 0; j < board.length; j++) {
          if (board[j].status !== cur_board) {
            // update the status
            axios({
              url: BASE_URL + "update-applicant-status",
              method: 'post',
              headers: { 
                'Accept': 'application/json',
                'Content-Type': 'application/json' },
              data: {
                'contact': board[j].contact,
                'status': cur_board
              }
            });
          }
        }
        
      }
    }



  },

}

export class Card {
  constructor(name, education, contact) {
    this.name = name;
    this.education = education;
    this.contact = contact;
    this.status = "Applied";
    this.rate = 0;
    this.reviewed = false;
    this.comments = [
      
    ]
  }

  renderCard() {
    return (
      "<h5>" + this.name + "</h5>" +
      "<span>" + this.education + "    |    " + "</span>" +
      "<span>" + this.contact + "    |    " + "</span>" +
      "<span>Avg. Rating: " + this.rate + "</span>" 
    )
  }

}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
/* light stylings for the kanban columns */
.kanban-column {
  min-height: 300px;
}
</style>
