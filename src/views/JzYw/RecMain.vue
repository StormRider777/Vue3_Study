<template>
    <table width="90%" style="margin: 1rem auto;">
        <tr><td><el-button type="primary">购货</el-button></td><td><el-button type="warning">付货款</el-button></td></tr>
        <tr><td><el-button type="success">销货</el-button></td><td><el-button type="danger">收货款</el-button></td></tr>
        <tr><td><el-button color="#626aef">费用</el-button></td><td></td></tr>
    </table>
</template>

<script>
    export default {
        name: "RecMain"
    }
</script>

<style scoped>
    tr{
        height: .8rem;
    }
    td{
        text-align: center;
        width:50%;
    }
    .el-button{
        height: .62rem;
        width: 90%;
    }
</style>