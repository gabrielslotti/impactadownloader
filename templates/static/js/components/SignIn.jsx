import React, { Component } from 'react';
import FacebookLogin from 'react-facebook-login';
import { FacebookLoginButton, GithubLoginButton } from "react-social-login-buttons";
import Modal from 'react-bootstrap/Modal';
 
export default class SignIn extends Component {
    constructor(props) {
        super(props);
        this.state = {showModal: false};
        this.showModalState = this.showModalState.bind(this);
        this.hideModalState = this.hideModalState.bind(this);
    }

    showModalState() {
        this.setState({showModal: true})
    }

    hideModalState() {
        this.setState({showModal: false})
    }

    render() {
        const modal = this.state.showModal ? (
            <Modal show={true}>
                <Modal.Header closeButton onClick={this.hideModalState}>Faça o Login</Modal.Header>
                <Modal.Body>
                    <FacebookLoginButton onClick={() => alert("Hello World")} />
                    <GithubLoginButton onClick={() => alert("Hello World")} />
                </Modal.Body>
                <Modal.Footer>
                </Modal.Footer>
            </Modal>
        ) : null;

        return (
            <header>
                <nav class="navbar navbar-dark bg-dark">
                    <a class="navbar-brand" href="#">Homepage</a>
                    <ul class="navbar-nav">
                        <li class="nav-item active">
                            <a class="nav-link" onClick={this.showModalState}>Login</a>
                            {modal}
                        </li>
                    </ul>
                </nav>
            </header>
        );
    }
}