import React, { useState, useEffect } from 'react';
import PropTypes from "prop-types";

const Navigation = (props) => {
    const [user, setUser] = useState();

    useEffect(() => {
        $.get(props.userDetailApiEndpoint, (data) => {
            setUser(data);
        });
    }, []);

    return <>
        <div className = "navbar-nav" id = "navbar-nav">
            {
                user ?
                    <div className = "d-flex align-self-center">
                        <a className = "slide-in-link link-light" role = "button" data-bs-toggle = "offcanvas" href = "#offcanvasRight" aria-controls = "offcanvasRight">
                            <h5 className = "slide-in-text slide-in-text-left">{ user.email }</h5>
                            <span className = "bi bi-person-circle"></span>
                        </a>
                    </div> :
                    <div className = "hstack gap-3">
                        <a className = "fs-6 link-light" href = { props.loginUrl }>Log in</a>
                        <div className = "vr"></div>
                        <a className = "fs-6 link-light" href = { props.registerUrl }>Sign up</a>
                    </div>
            }
        </div>
    </>;
};

Navigation.propTypes = {
    loginUrl: PropTypes.string,
    registerUrl: PropTypes.string,
    userDetailApiEndpoint: PropTypes.string,
};

export default Navigation;