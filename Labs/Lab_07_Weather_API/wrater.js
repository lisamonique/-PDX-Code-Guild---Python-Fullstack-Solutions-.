




let app = new Vue({
    el: '#app',
    data: {
        latitude: '',
        longitude: '',
        display: '',
        dt: '',
        temp: '',
        humidity: '',
    },
    methods: {
        getLocation: async function () {
            navigator.geolocation.getCurrentPosition(position => { 
            this.latitude = "Latitude: " + position.coords.latitude
            this.longitude = "Longitude: " + position.coords.longitude
            })
        }
    },    

    created: async function () {
        const response = await axios({
            method: 'get',
            url: 'https://api.openweathermap.org/data/2.5/onecall',
            params: {
                appid: API_KEY
            }
        })

        console.log(response)
    },
    // watch: {
    //     lat: async function () {
    //         let response = await axios({
    //             method: 'get',
    //             url: 'https://api.openweathermap.org/data/2.5/onecall',
    //             params: {
    //                 lat: this.lat,
    //                 lon: this.lon,
    //                 exclude: 'hourly,daily,minutely',
    //                 appid: API_KEY,
    //                 units: 'imperial'
    //             }
    //         })
    //     }
    // }
})