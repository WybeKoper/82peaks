import Link from 'next/link';
import React from 'react';
import Typed from "react-typed"
import Image from 'next/image';
import { AiOutlineMail } from 'react-icons/ai';
import { AiFillInstagram } from 'react-icons/ai';
import { FaGithub, FaLinkedinIn } from 'react-icons/fa';
import PersonalImg from '../public/assets/mountain_7.png';

const Main = () => {
  return (
    <div id='home' className='w-full h-screen text-center'>
      <div className='max-w-[1240px] pt-24 w-full h-full mx-auto p-2 justify-center items-center background-color: rgb(153, 153, 255)'>
        <div>
        <div className="relative mx-auto w-100 h-100 img-shape ">
        <Image src={PersonalImg} className="img-shape background-color: rgb(153, 153, 255)"></Image>
        </div>
        
        <div>
          <h1 className='py-4 text-2xl text-black'>
            Find the 4000m alpine peak with the best weather forecast. 
          </h1>


          
          </div>

        </div>
      </div>

    </div>
  );
};

export default Main;
