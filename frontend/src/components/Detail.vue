<template>
<div>
  <!-- Basic Info -->
    <p> {{$router.params.contact}} </p>
    <div v-html="card.renderCard()"></div>
    <!-- Rate -->
    <FormulateForm v-model="tempRate" @submit="card.submitRate(tempRate)">
    <FormulateInput class="col-1 px-1" name="rate" placeholder="Enter your rate" validation="required" />
    <FormulateInput class="col-1" type="submit" name="rate" label="Rate" validation="required" />
    </FormulateForm>
</div>
</template>

<script>
import { BASE_URL } from '../url';
import Card from './Card';
import $router from '../main';
import axios from '../main';

const card = new Card('Name', 'EDU', 123);
console.log(card);

export default {
    name: 'Kanban',
    data() {
       
        return {
            cardId: $router.params.contact,
            card: card,
            tempRate: 0
        }
    },
    mounted() {
        console.log("Come on" + card);
        axios
        .get(BASE_URL + "get-applicant")
        .then(response => this.card = response.data);
    },
    methods: {
        submitRate: function() {
            if (this.tempRate != 0) {
                var sum = this.card.rate * this.card.rateNumber;
                this.card.rateNumber++;
                this.card.rate = (sum + this.tempRate) / this.rateNumber;

                this.axios.post(BASE_URL + "add-rate", {
                    newRate: this.tempRate
                })
                .then((response) => {
                    this.card.rate = response.data.rate
                });
            } 
        }
    }




}
</script>

<style>

</style>