import React, {useEffect, useState} from 'react';
import axios from "axios";
import '../styles/tasks.css'
import {showToast} from "../tools/toast";

const Tasks = () => {
    const [tasks, setTasks] = useState([{'id': 0, 'answer_id': 0, 'date': '04/02/2022', 'title': 'Название',
        'description': 'Описание', 'status': 1}])

    const [firstName, setFirstName] = useState('')
    const [lastName, setLastName] = useState('')
    const [taskAnswer, setTaskAnswer] = useState('')

    async function getItemApi() {
        const response = await axios.get("http://192.168.1.88:5000/main/get_tasks")
        setTasks(response.data.data)
    }

    useEffect(() => {
        getItemApi()
    }, [])


    function hiddenAll(){
        tasks.forEach(item => {
            const a = document.getElementById('description ' + item.id)
            a.hidden = true
        })
    }

    function showTask(id){
        hiddenAll()
        const a = document.getElementById('description ' + id)
        a.hidden = false
        setTaskAnswer('')
    }

    async function sendAnswer(id){
        let data = new FormData()
        data.append('first_name', firstName)
        data.append('last_name', lastName)
        data.append('answer', taskAnswer)
        data.append('task_id', id)
        const response = await axios({
            url: "http://192.168.1.88:5000/add_answer",
            method: 'POST',
            data: data,
            headers: {
                Accept: 'application/json',
                'Content-Type': 'multipart/form-data',
            },
        })
        if (response.data.status) {
            showToast('success', 'Ответ отправлен успешно')
            return hiddenAll()
        }
        showToast('warn', response.data.warn)
    }

    return (
        <div className="Tasks-main">
            {tasks.map(item =>
                <div className="Tasks-task" key={item.id}>
                    <button className={"Tasks-btn"} onClick={() => showTask(item.id)}>
                        <div className="Task-div">
                            <div className={"Tasks-title"}>
                                <div className={"Task-id"}>#{item.id}</div>
                                <div>{item.title}</div>
                            </div>
                            <div><span>{item.date}</span></div>
                        </div>
                    </button>
                    <div id={"description " + item.id} className="Task-open" hidden={true}>
                        <p className="Task-desc">{item.description}</p>
                        <div className="Task-input-div">
                            <input className="Task-input" placeholder={"Имя"} value={firstName} onChange={e => setFirstName(e.target.value)} type="text"/>
                            <input className="Task-input" placeholder={"Фамилия"} value={lastName} onChange={e => setLastName(e.target.value)} type="text"/>
                        </div>
                        <div className="Task-input-div">
                            <textarea onKeyDown={(e) => {if (e.keyCode === 9) e.preventDefault();}}
                                      className="Task-input-text" rows="10" placeholder="Место для ввода ответа" value={taskAnswer}
                                      onChange={e => setTaskAnswer(e.target.value)}/>
                        </div>
                        <button className={'Tasks-btn-answer'} onClick={() => sendAnswer(item.id)}>
                            Предложить ответ
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
};

export default Tasks;