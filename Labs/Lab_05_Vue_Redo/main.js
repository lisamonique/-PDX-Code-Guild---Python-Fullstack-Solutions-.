let app = new Vue({
    el: '#app',
    data: {
        secretNumber: 0,
        counter: 0,
        guess: ''
    },

    methods: {
        guessNumber: function () {
            let number = parseInt(this.secretNumber)
            let random = Math.floor(Math.random () * 10) + 1

            if (number === random) {
                this.guess = "WOW!!! You guessed the secret number"
            }

            else if (number < random) {
                this.guess = "Your guess was too low!"
                
            } 
            
            else if (number > random) {
                this.guess = "Your guess was too high!"
            }

            else {
                this.guess = "Out of Attempts"
            }                  
        },
    }
    
})