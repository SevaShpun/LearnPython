import React, {useState} from 'react';
import '../styles/tasks.css'
import axios from "axios";
import {showToast} from "../tools/toast";


const TaskRequest = () => {

    const [taskTitle, setTaskTitle] = useState('')
    const [taskDescription, setTaskDescription] = useState('')
    const [taskStartCode, setTaskStartCode] = useState('')
    const [taskComment, setTaskComment] = useState('')


    async function sendAnswer(){
        let data = new FormData()
        data.append('title', taskTitle)
        data.append('description', taskDescription)
        data.append('start_code', taskStartCode)
        data.append('comment', taskComment)
        const response = await axios({
            url: "https://api.imsr.su/add_request",
            method: 'POST',
            data: data,
            headers: {
                Accept: 'application/json',
                'Content-Type': 'multipart/form-data',
            },
        })
        if (response.data.status) {
            showToast('success', 'Ответ отправлен успешно')
            return clearAll()
        }
        showToast('warn', response.data.warn)
    }

    function clearAll() {
        setTaskTitle('')
        setTaskDescription('')
        setTaskStartCode('')
        setTaskComment('')
    }


    return (
        <div>
            <div className={'task_tmp_req_two'}>
                <h1 className={'task-t-t-teq'}>Предложить свое задание</h1>
                <p className={'task-t-teq'}>Для того что бы предложить свое задание просто заполните поля ниже и нажмите на кнопку "Предложить задание".
                    После успешного добавления задания оно не появится на главной, а уйдет на проверку и только в случае если все хорошо его увидят все.</p>
            </div>
            <div className={'task_tmp_req'}>
                <h5 className={"task-req-text"}>Заголовкок задания:</h5>
                <input className="task-request-text" placeholder={"Обязательное поле с названием."} value={taskTitle} onChange={e => setTaskTitle(e.target.value)} type="text"/>
                <h5 className={"task-req-text"}>Задание:</h5>
                <textarea onKeyDown={(e) => {if (e.keyCode === 9) e.preventDefault();}}
                          className="task-request-text" rows="8" placeholder="Поле не может быть пустым." value={taskDescription}
                          onChange={e => setTaskDescription(e.target.value)}/>
                <h5 className={"task-req-text"}>Начальный код:</h5>
                <textarea onKeyDown={(e) => {if (e.keyCode === 9) e.preventDefault();}}
                          className="task-request-text" rows="8" placeholder="Начальный код и тесты (если они нужны, если нет оставьте поле пустым)" value={taskStartCode}
                          onChange={e => setTaskStartCode(e.target.value)}/>
                <h5 className={"task-req-text"}>Комментарий</h5>
                <textarea onKeyDown={(e) => {if (e.keyCode === 9) e.preventDefault();}}
                          className="task-request-text" rows="3" placeholder="В комментарии можно оставить ваше имя либо информацию которую считаете нужной. Комментарий не будет виден другим пользователям." value={taskComment}
                          onChange={e => setTaskComment(e.target.value)}/>
                <button className={'Tasks-btn-req'} onClick={() => sendAnswer()}>
                    Предложить задание
                </button>
            </div>
        </div>
    );
};

export default TaskRequest;