<template>
    <div class="registerForm">
        <h1>EStoy aqui</h1>
        {{ info }}
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'RegisterForm',
    data() {
        return {
            info: null
        }
    },
    mounted () {
        axios
        .get('http://localhost:8000/api/v1/user/')
        .then(response => (this.info = response))
    }
}
</script>
