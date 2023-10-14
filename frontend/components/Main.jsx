import Link from 'next/link';
import React, { useState }  from 'react';

import Typed from "react-typed"
import Image from 'next/image';
import { AiOutlineMail } from 'react-icons/ai';
import { AiFillInstagram } from 'react-icons/ai';
import { FaGithub, FaLinkedinIn } from 'react-icons/fa';
import PersonalImg from '../public/assets/mountain_7.png';
import Picker from './Picker';
import CommentsPage from './Commentloader';
import Home from './Commentloader';
import PickDates from './PickDates';



const Main = () => {
  return (
    <div id='home' className='w-full h-screen text-center'>
      <div className='max-w-[1240px] pt-24 w-full h-full mx-auto p-2 justify-center items-center'>
        <div>
        <h1 className='py-4 text-2xl text-black font-bold'>
            Find the 4000m alpine peak with the best weather forecast
          </h1>
        <div className="relative mx-auto w-100 h-100 img-shape ">
        <Image src={PersonalImg} className="img-shape"></Image>
        </div>
        
        <div>
          <PickDates/>
        </div>
        {/* <div className='flex items-center justify-center'>
          <div>
            <Picker className="py-4"/>
          </div>
          <div className='pl-5'>
          <CommentsPage className="py-4"/>
          </div>
        </div> */}
        </div>
      </div>

    </div>
  );
};

export default Main;
