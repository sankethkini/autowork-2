import React from "react";
import { Button, Form, FormGroup, Label, Input,Navbar} from 'reactstrap';
import axios from 'axios';
import Result from './Result';
import ReactDom from 'react-dom';
import Front from './Front';
export default class hyundai extends React.Component{
    constructor(props){
        super(props);
        this.state={
            loc:1,
            yr:2011,
            kd:40000,
            ft:2,
            tr:1,
            ot:1,
            ml:22,
            eng:1,
            po:70,
            st:5,
            np:7.5,
            md:2,
            res:{},
            disp:0
        }
        this.myChangeHandler = this.myChangeHandler.bind(this);
        this.mySubmitHandler = this.mySubmitHandler.bind(this);
        this.myHomehandler = this.myHomehandler.bind(this);
        this.myFunction=this.myFunction.bind(this);
    
    }
   async myFunction(){
               let url1="http://127.0.0.1:8000/apim/?&loc="+Number(this.state.loc)+"&yr="+Number(this.state.yr)+"&kd="+Number(this.state.kd)+"&ft="+Number(this.state.ft)+"&tr="+Number(this.state.tr)+"&ot="+Number(this.state.ot)+"&ml="+Number(this.state.ml)+"&eng="+Number(this.state.eng)+"&po="+Number(this.state.po)+"&st="+Number(this.state.st)+"&np="+Number(this.state.np)+"&md="+Number(this.state.md);
               
              await axios.get(url1)
              .then((res)=>{
                  console.log(res)
                  this.setState({res:res.data.result})
                  console.log(this.state.res)
              }
              )
             .catch((error)=>{
                 console.log(error);
             })
             this.setState({disp:1});
    }
    myChangeHandler(event){
            let nam = event.target.name;
            let val = event.target.value;
            this.setState({[nam]:val});
    }
    mySubmitHandler(event){
        event.preventDefault();
        this.myFunction();
    }
    myHomehandler(event){
        
        ReactDom.render(<Front />,document.getElementById('root'));
    }
render()
{
    return(
        <div className="container">
        
        <Navbar className="bg-dark justify-content-between">
           <button onClick={this.myHomehandler}><strong>Autowork</strong></button>
        </Navbar>    
        <br></br>
        <br></br>
        <h2>Enter your Car Details Here.</h2>
        <Form onSubmit={this.mySubmitHandler}>
            <FormGroup>
                <Label for="location">Select Location</Label>
                <Input id="location" type="select" name="loc" onChange={this.myChangeHandler}>
                    <option value="0">Ahamadabad</option>
                    <option value="1">Bengaluru</option>
                    <option value="2">Chennai</option>
                    <option value="3">Coimbatore</option>
                    <option value="4">Delhi</option>
                    <option value="5">Hyderabad</option>
                    <option value="6">Jaipur</option>
                    <option value="7">Kochi</option>
                    <option value="8">Kolkata</option>
                    <option value="9">Mumbai</option>
                    <option value="10">Pune</option>
                </Input>
            </FormGroup>
            <FormGroup>
                <Label for="year">Year of Buy</Label>
                <Input id="year" name="yr" type="text" placeholder="Ex. 2011" onChange={this.myChangeHandler}></Input>
            </FormGroup>
            <FormGroup>
                <Label for="kilometer">Kilometer Driven</Label>
                <Input id="kilometer" name="kd" type="text" placeholder="Ex. 35000" onChange={this.myChangeHandler}></Input>
            </FormGroup>
            <FormGroup>
                <Label for="fueltype">Fuel Type</Label>
                <Input id="fueltype" name="ft" type="select" onChange={this.myChangeHandler}>
                    <option value="1">Petrol</option>
                    <option value="2">Diesel</option>
                    <option value="3">LPG</option>
                </Input>
            </FormGroup>
            <FormGroup>
                <Label for="transmission">Transmission</Label>
                <Input id="transmission" name="tr" type="select" onChange={this.myChangeHandler}>
                    <option value="1">Manual</option>
                    <option value="2">Automatic</option>
                </Input>
            </FormGroup>
            <FormGroup>
                <Label for="ownertype">Owner Type</Label>
                <Input id="ownertype" name="ot" type="select" onChange={this.myChangeHandler}>
                    <option value="1">First</option>
                    <option value="2">Second</option>
                    <option value="3">Third</option>
                    <option value="4">Fourth And Above</option>
                </Input>
            </FormGroup>
            <FormGroup>
                <Label for="mileage">Mileage</Label>
                <Input id="mileage" name="ml" type="text" placeholder="Ex. 25" onChange={this.myChangeHandler}></Input>
            </FormGroup>
            <FormGroup>
                <Label for="engine">Engine</Label>
                <Input id="engine" name="eng" type="select" onChange={this.myChangeHandler}>
                    <option value="796">796</option>
                     <option value="998">998</option>
                     <option value="1061">1061</option>
                     <option value="1197">1197</option>
                     <option value="1248">1248</option>
                     <option value="1298">1298</option>
                     <option value="1373">1373</option>
                     <option value="1462">1462</option>
                </Input>
            </FormGroup>
            <FormGroup>
                <Label for="power">Power</Label>
                <Input id="power" name="po" type="text" placeholder="Ex. 86 in cc" onChange={this.myChangeHandler}></Input>
            </FormGroup>
            <FormGroup>
                <Label for="seat">Number of Seat</Label>
                <Input id="seat" name="st" type="text" placeholder="Ex. 5" onChange={this.myChangeHandler}></Input>
            </FormGroup>
            <FormGroup>
                <Label for="newprice">New Price</Label>
                <Input id="newprice" name="np" type="text" placeholder="Ex. 3.5 in Lakhs" onChange={this.myChangeHandler}></Input>
            </FormGroup>
            <FormGroup>
                <Label for="model">Model</Label>
                <Input id="model" name="md" type="select" onChange={this.myChangeHandler}>
                     <option value="1">Wagon R</option>
                     <option value="2">Ertiga</option>
                     <option value="3">Ciaz</option>
                     <option value="4">Swift</option>
                     <option value="5">Alto</option>
                </Input>
            </FormGroup>
            <FormGroup>
                <Button type="submit" color="success" disabled={false}>Submit</Button>
            </FormGroup>
        </Form>
        
        {this.state.disp && <Result res={this.state.res}/>}
        </div>
    );
}
}
