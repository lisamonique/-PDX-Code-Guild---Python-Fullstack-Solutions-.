let app = new Vue({
    data: {
        loading: true,
        lat: '',
        lon: '',
        display: '',
        dt: '',
        temp: '',
        humidity: '',
    },
    // methods: {
    //     getForecast: async function () {
    //         let response = await axios({
    //             url: ''
    //         })
    //     }
    // },
    
    created: function () {
        navigator.geolocation.getCurrentPosition(position => {
            this.lat = position.coords.latitude
            this.lon = position.coords.longitude
        })

        setTimeout(this.getForecast(), 1000)
    },
    watch: {
        lat: function () {
            console.log(this.lat, this.lon);
            this.loading = false
        },
    },
    el: '#app',
})