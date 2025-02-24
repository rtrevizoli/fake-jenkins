<template>
    <v-container>
        <h1>
            FRafaee Jenkins
        </h1>
      <v-form v-model="valid" @submit.prevent="submitForm">
        <v-text-field
          v-model="formData.bundleURL"
          label="Bundle URL"
          :rules="bundleURLRules"
          required
        ></v-text-field>


        <v-radio-group v-if="raioOk" v-model="formData.testSuit" inline>
            <v-radio label="Fast" value="fast"></v-radio>
            <v-radio label="Slow" value="slow"></v-radio>
        </v-radio-group>

        <li v-for="joke in jokes">
          {{ joke }}
        </li>

        <span
            class="headline"
            style="word-wrap: break-word; white-space: normal; overflow-wrap: break-word;"
        >
            Teste
        </span>

          <v-select
            :items="platformItems"
            label="Platform"
            v-model="formData.platform"
            :rules="platformRules"
            required
        ></v-select>
  
        <v-btn :disabled="!valid" type="submit" color="primary">Submit</v-btn>
      </v-form>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        valid: false,
        formData: {
          bundleURL: '',
          testSuit: "fast",
          platform: '',
        },
        raioOk: false,
        bundleURLRules: [(v) => !!v || 'This field is required'],
        platformRules: [(v) => !!v || 'This field is required'],
        platformItems: ["Tractor", "Combine", "Sprayer"],
        jokes: ['123']
      };
    },
    mounted() {
      this.getAPIJoke();
    },
    methods: {
      async submitForm() {
        try {
            console.log("RTX => Bundle URL: " + this.formData.bundleURL)
            console.log("RTX => Test Suit: " + this.formData.testSuit)
            console.log("RTX => Platform: " + this.formData.platform)

            // Sending the form data to the API
            const response = await axios.post('https://your-api-endpoint.com/submit', this.formData);
          
            // Handle the response (e.g., show a success message)
            console.log('Form submitted successfully:', response.data);
            this.$toast.success('Form submitted successfully');
        } catch (error) {
          // Handle any errors (e.g., show an error message)
          console.error('Error submitting form:', error);
          this.$toast.error('Failed to submit form');
        }
      },
      async getAPIJoke() {
      try {
        const response = await axios.get("https://api.chucknorris.io/jokes/random");
        this.jokes = [... [response.data.value]]
        console.log("RTX => ", response.data.value)
      } catch (e)
      {
        console.error(e)
      }
    }
    },

  };
  </script>
  
  <style scoped>
  /* Optional styles */
  </style>
  