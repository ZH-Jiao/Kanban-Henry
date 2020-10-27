<template>
<div class="b-container mt-5 mx-5">

    
      <FormulateForm v-model="formValues" @submit="handleSubmit">
        <FormulateInput name="name" label="Name" validation="required" />
        <FormulateInput name="education" label="Education" validation="required" />
        <FormulateInput name="contact" label="Contact" validation="required|number" />
        <FormulateInput type="submit" label="Add Applicant"/>
      </FormulateForm>
    


    <div class="row mt-4">
      <div class="col-4">
        <div class="p-2 alert alert-secondary">
          <h3>{{boardName[0]}}</h3>
          <!-- Backlog draggable component. Pass arrBackLog to list prop -->
          <draggable
            class="list-group kanban-column"
            :list="listBoard[boardName[0]]"
            group="tasks"
          >
            <div
              class="list-group-item"
              v-for="element in listBoard[boardName[0]]"
              :key="element.name"
            >
              <!-- {{ element.name }} -->
              <!-- Basic Info -->
              <div v-html="element.renderCard()"></div>

              <!-- Collaps Detail -->
              <b-button v-b-toggle.collapse-1 variant="primary">Expand Detail</b-button>
              <b-collapse id="collapse-1" class="mt-2">
                <b-card>
                  <!-- Rate -->
                  <FormulateForm class="row" v-model="tempRate" @submit="submitRate(element.contact)">
                  <FormulateInput class="col" name="rate" placeholder="Enter your rate" validation="required" />
                  <FormulateInput class="col" type="submit" name="rate" label="Rate" validation="required" />
                  </FormulateForm>
                </b-card>
                <b-card>
                  <p>Comment</p>
                  <b-list-group>
                    <b-list-group-item class="d-flex align-items-center" v-for="comment in element.comments" v-bind:key="comment.author">
                      <b-avatar class="mr-3"></b-avatar>
                      <span class="mr-auto">{{comment.author}}</span>
                      <span class="mr-auto">{{comment.content}}</span>
                    </b-list-group-item>
                  </b-list-group>
                   <!-- Add Comment -->
                  <FormulateForm class="row" v-model="tempRate" @submit="card.submitRate(tempRate)">
                    <FormulateInput class="col-2" name="rate" placeholder="Reviewer" validation="required" />
                    <FormulateInput class="col" name="rate" placeholder="Enter your comment" validation="required" />
                    <FormulateInput class="col" type="submit" name="rate" label="Comment" validation="required" />
                  </FormulateForm>
                </b-card>
              </b-collapse>

            </div>
          </draggable>
        </div>
      </div>

      <div class="col-4">
        <div class="p-2 alert alert-primary">
          <h3>{{boardName[1]}}</h3>
          <!-- In Progress draggable component. Pass arrInProgress to list prop -->
          <draggable
            class="list-group kanban-column"
            :list="listBoard[boardName[1]]"
            group="tasks"
          >
            <div
              class="list-group-item"
              v-for="element in listBoard[boardName[1]]"
              :key="element.name"
            >
              <div v-html="element.renderCard()"></div>
            </div>
          </draggable>
        </div>
      </div>

      <div class="col-4">
        <div class="p-2 alert alert-warning">
          <h3>{{boardName[2]}}</h3>
          <!-- Testing draggable component. Pass arrTested to list prop -->
          <draggable
            class="list-group kanban-column"
            :list="listBoard[boardName[2]]"
            group="tasks"
          >
            <div
              class="list-group-item"
              v-for="element in listBoard[boardName[2]]"
              :key="element.name"
            >
              <div v-html="element.renderCard()"></div>
            </div>
          </draggable>
        </div>
      </div>

      <div class="col-4">
        <div class="p-2 alert alert-success">
          <h3>{{boardName[3]}}</h3>
          <!-- Done draggable component. Pass arrDone to list prop -->
          <draggable
            class="list-group kanban-column"
            :list="listBoard[boardName[3]]"
            group="tasks"
          >
            <div
              class="list-group-item"
              v-for="element in listBoard[boardName[3]]"
              :key="element.name"
            >
              <div v-html="element.renderCard()"></div>
            </div>
          </draggable>
        </div>
      </div>

       <div class="col-4">
        <div class="p-2 alert alert-success">
          <h3>{{boardName[4]}}</h3>
          <!-- Done draggable component. Pass arrDone to list prop -->
          <draggable
            class="list-group kanban-column"
            :list="listBoard[boardName[4]]"
            group="tasks"
          >
            <div
              class="list-group-item"
              v-for="element in listBoard[boardName[4]]"
              :key="element.name"
            >
              <div v-html="element.renderCard()"></div>
            </div>
          </draggable>
        </div>
      </div>

       <div class="col-4">
        <div class="p-2 alert alert-success">
          <h3>{{boardName[5]}}</h3>
          <!-- Done draggable component. Pass arrDone to list prop -->
          <draggable
            class="list-group kanban-column"
            :list="listBoard[boardName[5]]"
            group="tasks"
          >
            <div
              class="list-group-item"
              v-for="element in listBoard[boardName[5]]"
              :key="element.name"
            >
              <div v-html="element.renderCard()"></div>
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
      tempRate: 0
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
      this.getAllApplicants();
    },

    submitRate(contact) {
      axios({
        url: BASE_URL + "add-rate",
        method: 'post',
        headers: { 
          'Accept': 'application/json',
          'Content-Type': 'application/json' },
        data: {
          contact: contact,
          newRate: this.tempRate
        }
      });
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
        for (entry of response.data) {
          var card = new Card(entry.name, entry.education, entry.contact);
          card.rate = entry.rate;
          this.listBoard[entry.status].push(card)
        }
      })
    },

    refreshList() {
      var n = null;
      for (n of this.boardName) {
        this.listBoard[n] = []
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
    this.comments = [
      {author: 'Manager', content: "He is so good"},
      {author: 'HR', content: "He is so good"},
      {author: 'Head HR', content: "He is so good"},
      {author: 'CTO', content: "He is so good"},
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
