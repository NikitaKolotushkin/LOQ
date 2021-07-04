import React, { Component } from "react";
// import { TextField, Button, Grid, Typography } from "@material-ui/core";
import { Link } from "react-router-dom";

export default class ProfilePage extends Component {
  constructor(props) {
    super(props);
    // this.state = {
    //   roomCode: "",
    //   error: "",
    // };
    // this.handleTextFieldChange = this.handleTextFieldChange.bind(this);
    // this.roomButtonPressed = this.roomButtonPressed.bind(this);
  }

  render() {
    return (
        <div>
            <div className="user_info">
                <div className="container">
                    <img src="/assets/img/logo.jpg" alt="" className="avatar"/>
                        <h1 className="name">Козлов Степан</h1>
                        <h3 className="status">LOQ #1</h3>
                </div>
            </div>

            <div className="user_content">
                <div className="container">
                    <div className="dark_block"></div>
                    <input type="text" name="vk_link" id="" placeholder="Ссылка на Ваш профиль VK"/>

                        <div className="content__block">
                            <h3 className="content__title">Основная информация</h3>
                            <div className="content__row">
                                <p className="text__left">Деятельность</p>
                                <p className="text__right">Маркетолог</p>
                            </div>
                            <div className="content__row">
                                <p className="text__left">Дата рождения</p>
                                <p className="text__right">7 октября</p>
                            </div>
                            <div className="content__row">
                                <p className="text__left">Жительство</p>
                                <p className="text__right">Москва</p>
                            </div>
                            <div className="content__row">
                                <p className="text__left">Семейный статус</p>
                                <p className="text__right">В разводе</p>
                            </div>
                        </div>

                        <div className="content__block">
                            <h3 className="content__title">Образование</h3>
                            <div className="content__row">
                                <p className="text__left">Языки</p>
                                <p className="text__right">Русский, <br/>Немецкий</p>
                            </div>
                            <div className="content__row">
                                <p className="text__left">ВУЗ</p>
                                <p className="text__right">МГУ</p>
                            </div>
                            <div className="content__row">
                                <p className="text__left">Школа</p>
                                <p className="text__right">Лицей ВШЭ</p>
                            </div>
                        </div>

                </div>
            </div>

        </div>
    );
  }

  // handleTextFieldChange(e) {
  //   this.setState({
  //     roomCode: e.target.value,
  //   });
  // }
  //
  // roomButtonPressed() {
  //   const requestOptions = {
  //     method: "POST",
  //     headers: { "Content-Type": "application/json" },
  //     body: JSON.stringify({
  //       code: this.state.roomCode,
  //     }),
  //   };
  //   fetch("/api/join-room", requestOptions)
  //     .then((response) => {
  //       if (response.ok) {
  //         this.props.history.push(`/room/${this.state.roomCode}`);
  //       } else {
  //         this.setState({ error: "Room not found." });
  //       }
  //     })
  //     .catch((error) => {
  //       console.log(error);
  //     });
  // }
}
