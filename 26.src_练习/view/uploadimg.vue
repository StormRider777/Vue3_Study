<template>
    <h2>上传图片</h2>
    <hr>
    <el-upload
            v-model:file-list="fileList"
            action="/dataserver/app01/uploadimg/"
            list-type="picture"

            :on-preview="handlePictureCardPreview"
            :on-remove="handleRemove"
            :on-success="refreshimgs"
    >
        <el-icon>
            <Plus/>
        </el-icon>
    </el-upload>
    <hr>
    <div v-for="(item,index) in imgfiles" :id="'view_imgdiv_'+index.toString()"
         style="width: 150px;height: 158px;border-radius: 5px;border: 1px solid gray;margin: 10px 10px;
                display: inline-grid;justify-content: center;align-items: center;padding: 1px 1px">
        <img :src="'/dataserver/static/app01/upload/'+item" alt="" style="width: 100%;height: 120px;object-fit:contain">

        <el-button type="warning" @click="deleimg(item,index)" style="width: 140px;margin:2px auto" >
            <el-icon><Delete /></el-icon>
            删除
        </el-button>
    </div>
    <el-dialog v-model="dialogVisible" title="图片预览" width="500px">
            <img w-full :src="dialogImageUrl" alt="Preview Image"
                 style="width: 100%;height: 100%;object-fit: cover;border-radius: 5px;box-shadow: 0 0 3px 3px grey">
    </el-dialog>
</template>

<script>
    import { ref,onMounted } from 'vue'
    import { Plus } from '@element-plus/icons-vue'
    import {ElMessage} from 'element-plus'
    import axios from 'axios'
    export default {
        name: "uploadimg",
        setup(){
            const fileList = ref([])
            const dialogImageUrl = ref('')
            const dialogVisible = ref(false)

            const handleRemove=(uploadFile, uploadFiles)=>{
                console.log(uploadFile, uploadFiles)

            }

            const handlePictureCardPreview=(uploadFile)=>{
                    dialogImageUrl.value = uploadFile.url
                    dialogVisible.value = true
            }
            onMounted(()=>{
                getfiles()
            })
            const imgfiles=ref([])

            const refreshimgs=(upf,f)=>{
                //console.log(upf,f)
                getfiles()
                console.log(fileList)
                //console.log(imgfiles.value)
            }

            let getfiles=()=>{
                axios.get('/dataserver/app01/getimgs/').then(res=>{
                    imgfiles.value=res.data
                })
            }

            let deleimg=(fname,index)=>{
                // let fd=new FormData()
                // fd.append('fname',fname)
                axios({
                    method:'get',
                    url: '/dataserver/app01/deleimg/',
                    params: {fname:fname}
                }).then(res=>{
                    if (!res.data.res){
                        ElMessage({message:'发生错误:'+res.data.msg,type:'warning'})
                    }else{
                        ElMessage({message:'删除文件:'+fname+'成功!',type:'success'})
                        let divno='view_imgdiv_'+index.toString()
                        document.getElementById(divno).remove()
                    }

                }).catch(e=>{
                    ElMessage({message:'发生错误:'+e.message,type:'error'})
                    console.log(e.message)
                })
            }


            return {fileList,dialogImageUrl,dialogVisible,handlePictureCardPreview,handleRemove,imgfiles,refreshimgs,deleimg}
        }
    }
</script>

<style scoped>
.el-dialog{
    width: 200px;
    height: 200px;
}
</style>