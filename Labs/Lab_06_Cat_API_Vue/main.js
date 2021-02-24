
let app = new Vue({
    el: '#app',
    data: {
        catUrl: '',
        categories: [],
        selectedCategory: ''
    },
    methods: {
        getCatImage: async function () {
            let response = await axios({
                method: 'get',
                url: 'https://api.thecatapi.com/v1/images/search',
                params: {
                    category_ids: this.selectedCategory
                }
            })
            this.catUrl = response.data[0].url
        }
    },
    created: async function () {
        let response = await axios({
            method: 'get',
            url: 'https://api.thecatapi.com/v1/categories'
        })
        this.categories = response.data
    }
})