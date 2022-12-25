<template>
    <div style="width: 100%;height: 100%">
        <div style="display:flex;justify-content: left;align-items: center">
            <el-button type="primary" @click="AddChildKm">增加下级</el-button>
            <!--@click="append('child')"-->
            <el-button type="success" @click="AddBrotherKm">增加同级</el-button>
            <!--@click="append('brother')"-->
            <el-button type="primary" @click="UpdateKm">修改科目</el-button>
            <el-button type="warning" @click="DeleKm">删除科目</el-button>
             <!--@click="remove"-->

        </div>
        <div style="border: 1px solid darkgrey;margin-top: 0.05rem;border-radius: 5px;margin-bottom: 0.1rem;overflow: hidden">
            <el-tree ref="treeRef"
                    :data="treedata.data"
                    :highlight-current="true"
                    node-key="id"
                    @node-click="handleNodeClick"
            >
                <template #default="{ node, data }">
                    <span class="custom-tree-node">
                        <span v-text="data.kmbm+' '+data.kmmc"></span>
                        <span v-text="data.qcje=='0.00'?'':parseFloat(data.qcje).toLocaleString('zh', { minimumFractionDigits: 2, useGrouping: true })"></span>
                    </span>
                </template>
            </el-tree>

            <!--:props="treeProps"-->
            <!--:show-checkbox="true"-->
        </div>
        <el-drawer
                v-model="DialogStates[CurrentState.state].display"
                direction="rtl"
                :close-on-click-modal="false"
                :before-close="handleDialogClose"
                 size="85%"
                style="margin-top: 0.5rem;height: 90%">
            <template #header>
                <span><el-icon><EditPen /></el-icon><span v-text="DialogStates[CurrentState.state].title"></span></span>
            </template>
            <template #default>
                <div>
                    <table>
                        <tr><td class="inputlabel">科目编码:</td>
                            <td class="inputbox"><el-input :disabled="CurrentState.state=='updatenode' || CurrentState.state=='delenode'" v-model="EditData.kmbm" ></el-input></td></tr>
                        <tr><td class="inputlabel">科目名称:</td>
                            <td class="inputbox" ><el-input :disabled="!DialogStates[CurrentState.state].isEdit" v-model="EditData.kmmc"></el-input></td></tr>
                        <tr><td class="inputlabel">科目性质:</td><td class="inputbox">
                            <el-radio-group v-model="EditData.kmxz" :disabled="!DialogStates[CurrentState.state].isEdit">
                                <el-radio :label='1'>借方科目</el-radio>
                                <el-radio :label='2'>贷方科目</el-radio>
                            </el-radio-group>
                        </td></tr>
                        <tr v-show="(CurrentState.state=='updatenode' && CurrentNode.node.childNodes.length==0) || CurrentState.state=='addchild' || CurrentState.state=='addbrother'">
                            <td class="inputlabel">期初数量:</td>
                            <td class="inputbox" >
                                <el-input-number controls-position="right" :precision="3"
                                                 :disabled="!DialogStates[CurrentState.state].isEdit || EditData.zbqy"
                                                 v-model="EditData.qcsl">

                                </el-input-number></td>
                        </tr>
                        <tr  v-show="(CurrentState.state=='updatenode' && CurrentNode.node.childNodes.length==0) || CurrentState.state=='addchild' || CurrentState.state=='addbrother'"><td class="inputlabel">期初金额:</td>
                            <td class="inputbox" >
                                <el-input-number  controls-position="right" :precision="2"
                                                  :disabled="!DialogStates[CurrentState.state].isEdit || EditData.zbqy"
                                                  v-model="EditData.qcje">

                                </el-input-number></td>
                        </tr>
                        <tr><td class="inputlabel"></td>
                            <td class="inputbox" >
                                <el-checkbox v-model="EditData.zbqy" :disabled="!DialogStates[CurrentState.state].isEdit">账簿启用</el-checkbox>
                            </td>
                        </tr>

                        <tr><td colspan="2" style="color:red;font-size: 0.14rem">
                            <p>* 修改含有子科目的科目时,不出现期初数量,期初金额,不允许填入</p>
                            <p>* 启用账簿后,数量,和金额,不能再修改.</p>
                        </td></tr>
                    </table>
                </div>
            </template>
            <template #footer>
                <div style="display: flex;justify-content:right;align-items: center">
                    <el-button type="warning" @click="CurrentState.state='default'">
                        <el-icon><Close /></el-icon>
                        取消
                    </el-button>
                    <el-button type="success" @click="DialogYesBtn">
                        <el-icon><Select /></el-icon>
                        确认
                    </el-button>
                </div>
            </template>
        </el-drawer>
    </div>
</template>

<script>
    import {reactive,ref,onMounted} from 'vue'
    import {$get,$post} from "../../api/request"
    import {ElMessage,ElTree,ElMessageBox} from 'element-plus'
    export default {
        name: "SetKm",
        setup(){
            const treedata=reactive({
                data:[]
            })
            const treeProps=reactive({
                children: 'children',
                label: 'label',
            })
            const treeRef=ref(null)

            const EditData=reactive({
                id:null,
                _parent:null,
                kmbm:'',
                kmmc:'',
                kmxz:null,
                qcsl:0.000,
                qcje:0.00,
                zbqy:false,
            })

            const CurrentNode=reactive({
                data:null,
                node:null,
            })
            const DialogStates=reactive({
                default:{title:'默认',display:false,data:{id:null,_parentId:null,kmbm:null,kmmc:null,kmxz:null}},
                addbrother:{title:'增加同级科目',display:true,isEdit:true,data:{id:null,_parentId:null,kmbm:null,kmmc:null,kmxz:null}},
                addchild:{title:'增加子科目',display:true,isEdit:true,data:{id:null,_parentId:null,kmbm:null,kmmc:null,kmxz:null}},
                delenode:{title:'删除科目',display:true,isEdit:false,data:{id:null,_parentId:null,kmbm:null,kmmc:null,kmxz:null}},
                updatenode:{title:'修改科目',display:true,isEdit:true,data:{id:null,_parentId:null,kmbm:null,kmmc:null,kmxz:null}},
            })
            const CurrentState=reactive({
                state:'default',
            })

            const handleNodeClick = (data,treenode,node,enent) => {
                CurrentNode.data=data
                CurrentNode.node=treenode
                // console.log(CurrentNode.node)
            }
            onMounted(()=>{
                            $get('/jxc/getkm/',{nodeid:null}).then(res=>{
                                if (res.data.res){
                                    treedata.data=res.data.data
                                    // console.log(treedata.data)
                                }else{
                                    ElMessage({message:res.data.msg,type:'error',showClose:true})
                                }
                            })
                        })
            let handleDialogClose=(done)=>{
                done()
            }

            const append = (mtype) => {
                const data=CurrentNode.data
                if (mtype=='child'){
                    // path('addkm/', Kmviews.addKm, name='addkm'),  # POST
                    // data: kmmc,kmbm,kmxz,pid
                    if (data){
                        let pid=data.id
                        let node=CurrentNode.node
                        $post('/jxc/addkm/',{pid:EditData._parentId,kmmc:EditData.kmmc,kmbm:EditData.kmbm,kmxz:EditData.kmxz,qcsl:EditData.qcsl,qcje:EditData.qcje}).then(res=>{
                            // console.log('addchild:',res)
                            if (res.res){
                                const newNode = {
                                    id:res.data.id,
                                    _parentId:res.data._parentId,
                                    kmbm:res.data.kmbm,
                                    kmmc:res.data.kmmc,
                                    label: res.data.label,
                                    kmxz:res.data.kmxz,
                                    qcsl:res.data.qcsl,
                                    qcje:res.data.qcje,
                                    zbqy:res.data.zbqy,
                                }
                                if (!data.children) {
                                    data.children = []
                                }
                                data.children.push(newNode)
                                node.expand()
                                let nextnode=node.childNodes[node.childNodes.length-1]
                                // console.log(nextnode)
                                if (nextnode){
                                    treeRef.value.setCurrentNode(nextnode.data,true)
                                    // 1. 待被选中的节点 2. 是否展开父节点)
                                    CurrentNode.data=nextnode.data
                                    CurrentNode.node=nextnode
                                }
                                ElMessage({message:'添加成功:'+res.data.kmbm+' '+res.data.kmmc,type:'success',duration:100})
                            }else{
                                ElMessage({message:res.msg,type:'error',duration:3000})
                            }


                        })
                    }else{
                        ElMessage({message:'请选一个节点!',type:'warning',duration:2000})
                    }
                }else if ( mtype=='brother') {
                    if (data){
                        let pid=data._parentId
                        if (pid==null){
                            pid=0
                        }
                        let node=CurrentNode.node
                        $post('/jxc/addkm/',{pid:EditData._parentId,kmmc:EditData.kmmc,kmbm:EditData.kmbm,kmxz:EditData.kmxz,qcsl:EditData.qcsl,qcje:EditData.qcje}).then(res=>{
                            // console.log(res)
                            if (res.res){
                                const newNode = {
                                    id:res.data.id,
                                    _parentId:res.data._parentId,
                                    kmbm:res.data.kmbm,
                                    kmmc:res.data.kmmc,
                                    label: res.data.label,
                                    qcsl:res.data.qcsl,
                                    qcje:res.data.qcje,
                                    zbqy:res.data.zbqy,
                                }
                                const data=CurrentNode.node.parent.data
                                if (!data.children) {
                                    data.children = []
                                }
                                if (pid) {
                                    data.children.push(newNode)
                                }else{
                                    data.push(newNode)
                                }

                                let nextnode=node.parent.childNodes[node.parent.childNodes.length-1]
                                if (nextnode){
                                    treeRef.value.setCurrentNode(nextnode.data,true)
                                    // 1. 待被选中的节点 2. 是否展开父节点)
                                    CurrentNode.data=nextnode.data
                                    CurrentNode.node=nextnode
                                }
                                ElMessage({message:'添加成功:'+res.data.kmbm+' '+res.data.kmmc,type:'success',duration:100})
                            }else{
                                ElMessage({message:res.msg,type:'error',duration:3000})
                            }
                        })
                    }else{
                        ElMessage({message:'请选一个节点!',type:'warning',duration:1000})
                    }
                }
            }
            const remove = () => {
                const node=CurrentNode.node
                const data=CurrentNode.data
                if (data){
                    const parent=node.parent
                    var children=null
                    if (data._parentId==null){
                        children=parent.data
                    }else{
                        children= parent.data.children
                    }
                    // var children= parent.data.children || parent.data
                    const index = children.findIndex((d) =>{
                        return d.kmbm==data.kmbm
                    })

                    if (children[index]){
                        $get('/jxc/delekm/',{id:children[index].id}).then(res=>{
                            res=res.data
                            if (res.res){
                                ElMessage({message:'删除成功:'+children[index].kmbm+' '+children[index].kmmc,type:'success',duration:200})
                                children.splice(index, 1)
                                let nextnode=null
                                if (index>0){
                                    let nexti=index-1
                                    nextnode=parent.childNodes[nexti]
                                }else{
                                    nextnode=parent
                                }
                                treeRef.value.setCurrentNode(nextnode.data)
                                CurrentNode.data=nextnode.data
                                CurrentNode.node=nextnode
                            }else{
                                ElMessage({message:res.msg,type:'error',duration:2000})
                            }

                        })
                    }else{
                        ElMessage({message:'发生错误',type:'error',duration:3000,showClose:true})
                    }
                    // dataSource.value = [...dataSource.value]
                }else{
                    ElMessage({message:'请选一个节点!',type:'warning',duration:1000})
                }
            }
            const update=()=>{
                let fsdata={
                    id:EditData.id,
                    pid:EditData._parentId,
                    kmmc:EditData.kmmc,
                    kmbm:EditData.kmbm,
                    kmxz:EditData.kmxz,
                    qcsl:EditData.qcsl,
                    qcje:EditData.qcje,
                    zbqy:EditData.zbqy
                }
                $post('/jxc/updatekm/',fsdata).then(res=>{
                    if (res.res){
                        const newNode = {
                            id:res.data.id,
                            _parentId:res.data._parentId,
                            kmbm:res.data.kmbm,
                            kmmc:res.data.kmmc,
                            label: res.data.label,
                            kmxz:res.data.kmxz,
                            qcsl:res.data.qcsl,
                            qcje:res.data.qcje,
                            zbqy:res.data.zbqy,
                        }

                        //修改tree数据
                        index = treedata.findIndex(item=>{
                            return item.id=newNode.id
                        })
                        console.log(treedata[index],newNode)

                        CurrentNode.data=newNode
                        CurrentNode.node=treenode
                        ElMessage({message:'添加成功:'+res.data.kmbm+' '+res.data.kmmc,type:'success',duration:100})
                    }else{
                        ElMessage({message:res.msg,type:'error',duration:3000})
                    }
                })
            }

            let ValidData=()=>{

            }
            let DialogYesBtn=()=>{
                if (CurrentState.state=='delenode'){
                    ElMessageBox({
                        title:'确认删除',
                        message:`请确认,是否删除:<br><strong style="color:red;margin-left: 0.25rem">${EditData.kmbm}  ${EditData.kmmc}</strong> ?`,
                        dangerouslyUseHTMLString:true,
                        'close-on-click-modal':false,
                        draggable:true,
                        showCancelButton: true,
                        cancelButtonText:'取消',
                        confirmButtonText:'确定'
                    }).then(y=>{
                        remove()
                    }).catch(n=>{
                        // console.log(n)
                    })
                }else if(CurrentState.state=='addchild'){
                    // ElMessage('增加子科目 已保存')
                    append('child')
                }else if(CurrentState.state=='addbrother'){
                    // ElMessage('增加同级已保存')
                    append('brother')
                }else if(CurrentState.state=='updatenode'){
                    update()
                }
                CurrentState.state='default'

            }

            let AddChildKm=()=>{
                if (!CurrentNode.data){
                    ElMessage({message:'请选择一条记录!',type:'warning',duration:1000})
                    return false
                }
                EditData.id=null
                EditData._parentId=CurrentNode.data.id
                EditData.kmbm=''
                EditData.kmmc=''
                EditData.kmxz=1
                EditData.qcsl=0.000
                EditData.qcje=0.00
                EditData.zbqy=false
                if (!CurrentNode.data.id){
                    ElMessage({message:'请选择一条记录!',type:'warning',duration:1000})
                    return false
                }

                CurrentState.state='addchild'
            }
            let UpdateKm=()=>{
                if (!CurrentNode.data){
                    ElMessage({message:'请选择一条记录!',type:'warning',duration:1000})
                    return false
                }
                EditData.id=CurrentNode.data.id
                EditData._parentId=CurrentNode.data._parentId
                EditData.kmbm=CurrentNode.data.kmbm
                EditData.kmmc=CurrentNode.data.kmmc
                EditData.kmxz=CurrentNode.data.kmxz
                EditData.qcsl=parseFloat(CurrentNode.data.qcsl)
                EditData.qcje=parseFloat(CurrentNode.data.qcje)
                EditData.zbqy=CurrentNode.data.zbqy

                CurrentState.state='updatenode'
            }
            let DeleKm=()=>{
                if (!CurrentNode.data){
                    ElMessage({message:'请选择一条记录!',type:'warning',duration:1000})
                    return false
                }
                EditData.id=CurrentNode.data.id
                EditData._parentId=CurrentNode.data._parentId
                EditData.kmbm=CurrentNode.data.kmbm
                EditData.kmmc=CurrentNode.data.kmmc
                EditData.kmxz=CurrentNode.data.kmxz
                EditData.qcsl=parseFloat(CurrentNode.data.qcsl)
                EditData.qcje=parseFloat(CurrentNode.data.qcje)
                EditData.zbqy=CurrentNode.data.zbqy
                console.log(EditData)

                CurrentState.state='delenode'
            }
            let AddBrotherKm=()=>{
                if (!CurrentNode.data){
                    ElMessage({message:'请选择一条记录!',type:'warning',duration:1000})
                    return false
                }
                EditData.id=null
                EditData._parentId=CurrentNode.data._parentId
                EditData.kmbm=''
                EditData.kmmc=''
                EditData.kmxz=1
                EditData.qcsl=0.000
                EditData.qcje=0.00
                EditData.zbqy=false

                CurrentState.state='addbrother'
            }

            return {treedata,treeProps,treeRef,DialogStates,CurrentState,treeRef,EditData,CurrentNode,
                handleNodeClick,append,remove,handleDialogClose,DialogYesBtn,
                UpdateKm,DeleKm,AddBrotherKm,AddChildKm}
        }
    }
</script>

<style scoped>
     .el-button{
         width:0.7rem
     }
    .el-tree{
        font-weight: 600;
        font-size: 0.15rem;
    }
    :deep(.el-tree--highlight-current .el-tree-node.is-current) > .el-tree-node__content {
        background-color: darkblue !important;
        color:yellow;
    }
    tr{
        height: 0.5rem;
    }

     .custom-tree-node {
         flex: 1;
         display: flex;
         align-items: center;
         justify-content: space-between;
         font-size: 14px;
         padding-right: 8px;
     }
    :deep(input[type='number']){
        text-align: right;
    }
</style>