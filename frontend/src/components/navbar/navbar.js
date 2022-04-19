import { React, useState } from "react"
import { useNavigate } from "react-router-dom"

import "bootstrap-icons/font/bootstrap-icons.css"
import { Navbar, Container, Nav, Button } from "react-bootstrap"
import './navbar.scss';
import NavbarCartComponent from "../navbarcart/navbarcart"
import FilterComponent from "../filter/filter";

const NavbarComponent = () => {
    const navigate = useNavigate();
    const [filterTrigger, setFilterTrigger] = useState(false);

    return(
        <Navbar bg="dark" variant="dark" >
        <Container>
            <Navbar.Brand onClick={() => navigate(`/`)}>Home</Navbar.Brand>
            <Nav className="me-auto">
                <Nav.Link onClick={() => navigate(`/smartphones/`)}>Smartphones</Nav.Link>
                <Nav.Link onClick={() => navigate(`/laptops/`)}>Laptops</Nav.Link>
            </Nav>
            <Nav className='justify-content-end'>
                <Button onClick={() => setFilterTrigger(true)}>Filter</Button>
                <FilterComponent filterTrigger={filterTrigger} setFilterTrigger={setFilterTrigger}/>
                <NavbarCartComponent/>
            </Nav>
        </Container>
        </Navbar>
    )
}

export default NavbarComponent