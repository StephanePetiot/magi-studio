import React, { useState, useEffect } from 'react';
import PropTypes from "prop-types";

const Offcanvas = (props) => {
    const [user, setUser] = useState();

    useEffect(() => {
        $.get(props.userDetailApiEndpoint, (data) => {
            setUser(data);
        });
    }, []);

    const handleLogout = (event) => {
        event.preventDefault();
        $.post(props.logoutApiEndpoint, {}, (response) => {
            window.location.href = response.redirect_url;
        });
    };

    return <>
        {
            user ?
            <div>
                <div className = "offcanvas-header">
                    <h5 id = "offcanvasRightLabel"><span className = "bi bi-person-circle"></span> { user.email }</h5>
                    <button type = "button" className = "btn-close text-reset" data-bs-dismiss = "offcanvas" aria-label = "Close"></button>
                </div>
                <div className = "offcanvas-body">
                    <div className = "navbar-nav">
                        {
                            user.is_admin ?
                                <a className = "nav-link" href = "/admin/">Admin</a> :
                                null
                        }
                        <hr/>
                        <form action = { props.logoutApiEndpoint } method = "post" onSubmit = { handleLogout }>
                            <input type = "submit" className = "btn btn-primary" value = "Log Out"></input>
                        </form>
                    </div>
                </div>
            </div> :
            null
        }
    </>;
};

Offcanvas.propTypes = {
    userDetailApiEndpoint: PropTypes.string,
    logoutApiEndpoint: PropTypes.string,
};

export default Offcanvas;