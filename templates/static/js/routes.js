import React from 'react';
import { HashRouter, Route, hashHistory } from 'react-router-dom';
import Home from './components/Home';
import SignIn from './components/SignIn';

// import more components
export default (
    <HashRouter history={hashHistory}>
        <div>
            <Route path='/' component={SignIn} />
        </div>
    </HashRouter>
);