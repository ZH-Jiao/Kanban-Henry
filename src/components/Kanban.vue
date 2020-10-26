<template>
<div class="container mt-5">
    <div class="row">
      <div class="col form-inline">
        <b-form-input
          id="input-2"
          v-model="newApplicant"
          required
          placeholder="Enter new applicant's name"
          @keyup.enter="add"
        ></b-form-input>
        <b-button @click="add" variant="primary" class="ml-3">Add</b-button>
      </div>
    </div>

    
      <FormulateForm v-model="formValues" @submit="handleSubmit">
        <FormulateInput name="name" label="Name" validation="required" />
        <FormulateInput name="education" label="Education" validation="required" />
        <FormulateInput name="contact" label="Contact" validation="required|number" />
        <FormulateInput type="submit" label="Add Applicant"/>
      </FormulateForm>
    


    <div class="row mt-5">
      <div class="col-3">
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
              <div v-html="element.renderCard()"></div>
            </div>
          </draggable>
        </div>
      </div>

      <div class="col-3">
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

      <div class="col-3">
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

      <div class="col-3">
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

       <div class="col-3">
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

       <div class="col-3">
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

export default {
  name: 'Kanban',
  components: {
    draggable
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
      }
    }
  },
  methods: {
    add: function() {
      if (this.newApplicant) {
        this.listBoard['Applied'].push({name: this.newApplicant});
        this.newApplicant = "";
      }
    },
    handleSubmit() {
      console.log(this.formValues);
      var card = new Card(
        this.formValues['name'],
        this.formValues['education'],
        this.formValues['contact']
      );
      this.listBoard['Applied'].push(card);
      console.log(this.listBoard['Applied'])
    }
  }
}

class Card {
  constructor(name, education, contact) {
    this.name = name;
    this.education = education;
    this.contact = contact;
    this.status = "Applied";
    this.rate = 0;
    this.rateNumber = 0;
  }

  renderCard() {
    return (
      "<h5>" + this.name + "</h5>" +
      "<p>" + this.contact + "</br>" +
      this.education + "</br>" +
      "Rate: " + this.rate + "</p>" 
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
