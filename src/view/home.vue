<template>
    <div style="width: 500px;margin: 50px auto;border: 2px solid red">
            <el-button type="primary" @click="viewimg">
                <el-icon>
                    <StarFilled/>
                </el-icon>
                浏览图片
            </el-button>

            <el-button type="success" @click="uploadimg">
                <el-icon>
                    <Picture/>
                </el-icon>
                上传图片
            </el-button>

            <el-button type="warning" @click="explortExcel">
                <el-icon size="20px" color="blue">
                    <DocumentCopy/>
                </el-icon>
                表格数据导出EXCEL
            </el-button>

            <el-button type="warning" @click="goeltabs">
                <el-icon size="20px" color="blue">
                    <DocumentCopy/>
                </el-icon>
                Tabs标签页
            </el-button>
            <el-button type="success" @click="goelxsr">
                <el-icon size="20px" color="blue">
                    <DocumentCopy/>
                </el-icon>
                失信人
            </el-button>
    </div>
</template>

<script>
    import {useRouter} from 'vue-router'
    export default {
        name: "home",
        setup(){
            const  router=useRouter()
            let viewimg=()=>{
                router.push('/viewimg/')
            }
            let uploadimg=()=>{
                router.push('/uploadimg/')
            }
            let explortExcel=()=>{
                router.push('/explortExcel/')
            }
            let goeltabs=()=>{
                router.push('/myeltabs/')
            }
            let goelxsr=()=>{
                router.push('/sxr/')
            }
            return {uploadimg,viewimg,explortExcel,goeltabs,goelxsr}
        }
    }
</script>

<style scoped>
    .el-icon{
        font-size: 20px;
    }
    .el-button{
        height: 45px;
        width: 200px;
        margin-left: 30px;
        margin-top: 10px;
        margin-bottom: 10px;
    }
</style>