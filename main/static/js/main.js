
const domain = 'http://127.0.0.1:8000'


const registerUrl = domain + '/api/task'

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

async function tasks() {
    const response = await fetch(domain + '/api/task');
    const tasks = await response.json();

    const table = document.getElementById('task-table');
    const tbody = table.querySelector('tbody');

    tasks.forEach(task => {
        const row = document.createElement('tr');

        // Create and populate the table cells for each task property
        const runCell = document.createElement('td');
        const runButton = document.createElement('button');
        runButton.type = 'button';
        runButton.className = 'btn btn-run';
        runButton.textContent = 'Run task';
        
        // Attach a click event listener to the "Run task" button
        runButton.addEventListener('click', function() {
            const path = task.id;
            fetch(domain + '/api/task/execute/' + String(task.id))
            console.log('Running task with path:', path);
        });

        runCell.appendChild(runButton);

        const nameCell = document.createElement('td');
        nameCell.textContent = task.name;

        const scheduleCell = document.createElement('td');
        scheduleCell.textContent = task.schedule_param;

        const lastExecutionCell = document.createElement('td');
        lastExecutionCell.textContent = task.last_execution;

        const nextExecutionCell = document.createElement('td');
        nextExecutionCell.textContent = task.next_execution;

        const detailsCell = document.createElement('td');
        detailsCell.innerHTML = '<a href="#" class="btn btn-det">Details</a>';

        const deleteCell = document.createElement('td');
        deleteCell.innerHTML = '<button type="button" class="btn btn-del">Delete task</button>';

        // Append the cells to the row
        row.appendChild(runCell);
        row.appendChild(nameCell);
        row.appendChild(scheduleCell);
        row.appendChild(lastExecutionCell);
        row.appendChild(nextExecutionCell);
        row.appendChild(detailsCell);
        row.appendChild(deleteCell);

        // Append the row to the table body
        tbody.appendChild(row);
    });
}




