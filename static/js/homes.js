// document.querySelector(".title_p").style.display = "none"
document.addEventListener("DOMContentLoaded",()=>{
    const nameSearch = document.getElementById("search")
    const tag = document.querySelectorAll(".tag_btn")
    const project = document.querySelectorAll(".project")

    function filterProject(){
        const nameQuery = nameSearch.value.toLowerCase()

        project.forEach(projects =>{
            const name = projects.getAttribute('data-name')
            const nameMatch = name.includes(nameQuery)

            if(nameMatch){
                projects.style.display = ""
            }else if(nameSearch.value == ""){
                projects.style.display = ""
            }else{
                projects.style.display = "none"
            }
        })
    };

    tag.forEach(tag =>{
        tag.addEventListener("click",()=>{
            const selectedTag = this.innerHTML.toLowerCase()
            project.forEach(projects =>{
                const projectTag = projects.getAttribute("data-tags")
                if(projectTag.includes(selectedTag)){
                    projects.style.display = ""
                }else{
                    projects.style.display = "none"
                }
            })
        })
    })

    nameSearch.addEventListener("keyup",filterProject)
    nameSearch.addEventListener("input",filterProject)
})

const description = document.querySelectorAll(".project_description")
description.forEach((description)=>{
    let split_description = description.innerHTML.trim().split("")
    let new_description = split_description.toSpliced(29,split_description.length - 29,"...")
    
    description.innerHTML = new_description.join("")

})