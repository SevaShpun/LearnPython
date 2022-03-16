import React from 'react';
import {Link} from "react-router-dom";
import '../styles/navbar.css'

const NavBar = () => {
    return (
        <div>
            <ul className="menu cf">
                <Link to="/"><li>Главная</li></Link>
                <Link to="/request_task"><li>Предложка</li></Link>
                <Link to="/archive"><li>Архив</li></Link>
            </ul>
        </div>
    );
};

export default NavBar;