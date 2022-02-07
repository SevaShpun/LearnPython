import React, {useEffect, useState} from 'react';
import axios from "axios";
import '../styles/tasks.css'


const ArchiveTasks = () => {
    const [tasks, setTasks] = useState([])

    const [answer, setAnswer] = useState({'id': 0, 'task_id': 0, 'first_name': 'Имя', 'last_name': 'Фамилия',
        'answer': 'Ответа пока нет'})

    const [lastShow, setLastShow] = useState('')


    async function getItemApi() {
        const response = await axios.get("https://api.imsr.su/archive/get_tasks")
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

    async function getAnswer(id){
        const response = await axios.get("https://api.imsr.su/get_answer?id=" + id)
        setAnswer(response.data)
    }

    function showTask(id){
        if (id === lastShow) {
            setLastShow('')
            return hiddenAll()
        }
        setLastShow(id)
        hiddenAll()
        console.log(answer)
        const a = document.getElementById('description ' + id)
        a.hidden = false
    }

    return (
        <div className="Tasks-main">
            {tasks.map(item =>
                <div className="Tasks-task" key={item.id}>
                    <button className={"Tasks-btn"} onClick={() => {showTask(item.id)
                                                                    getAnswer(item.answer_id)}}>
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
                        <div>
                            <p className="Task-answer-name">Лучший ответ: {answer.first_name} {answer.last_name}</p>
                            <p className="Task-answer">{answer.answer}</p>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default ArchiveTasks;