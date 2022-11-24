<template>
    <div class="common-layout" style="min-width: 1000px">
        <el-container style="min-width: 1000px">
            <el-header height="60px">
                <HomeHeader></HomeHeader>
            </el-header>

            <el-container>
                <el-aside width="220px">
                    <HomeMenu></HomeMenu>
                </el-aside>
                <el-main>
                    <HomeMain></HomeMain>
                </el-main>
            </el-container>
            <el-footer height="40px">
                <HomeFooter></HomeFooter>
            </el-footer>
        </el-container>
    </div>
</template>

<script>
    import HomeFooter from "../../components/HomeFooter"
    import HomeHeader from "../../components/HomeHeader"
    import HomeMain from "../../components/HomeMain"
    import HomeMenu from "../../components/HomeMenu"

    export default {
        name: "Home",
        components:{HomeMenu,HomeHeader,HomeMain,HomeFooter},
        setup(){}
    }
</script>

<style>
    .el-container,.common-layout,#app,body,html{
        width: 100vw;
        height: 100vh;
        margin-top: 0;
        overflow: auto;
    }
    .el-header{
        background: linear-gradient(to right,skyblue,dodgerblue,royalblue,blue,darkblue);
        margin: 0 0 0 0;
        padding: 0 5px 0 5px;
        line-height: 60px;

    }
    .el-aside{
        background: #545c64;
    }
    .el-footer{
        background: #434343;
    }
    .el-main{
        background: whitesmoke;
    }
</style>