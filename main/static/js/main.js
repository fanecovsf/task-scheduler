
const registerUrl = 'http://127.0.0.1:8000/api/task'

function registerTask() {
    const name = document.getElementById("name").value
    const path = document.getElementById("path").value
    const desc = document.getElementById("description").value
    const schedule = document.getElementById("schedule_param").value
    
    if (name && path && desc && schedule) {
        const data = {
            "name":name,
            "path":path,
            "desc":desc,
            "schedule_param":schedule,
            "last_execution": null,
            "next_execution": null,
            "executions": 0,
            "active": false
        }

        console.log(data)

        const requestOptions = {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(data) 
        };

        fetch(registerUrl, requestOptions)
            .then(response =>{
                if (!response.ok) {
                    throw new Error('Error')
                }
                return response.json()
                }     
            )
            .then(data => {
                console.log('Resposta do servidor', data)
            })
            .catch(error => {
                console.error('Error:', error)
            })
        
    }

}




