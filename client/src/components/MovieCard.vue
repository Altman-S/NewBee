<template>
    <div>
        <h1>{{title}}</h1>
        <img :src="imgurl" :alt="title">
    </div>
    
</template>

<script>
export default {
    name:'MovieCard',
    props:{
        title:String,
        imgurl:String
    }
}
</script>