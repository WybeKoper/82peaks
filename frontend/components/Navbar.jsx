import Image from 'next/image';
import Link from 'next/link';
import React, { useState, useEffect } from 'react';
import { AiOutlineClose, AiOutlineMail, AiOutlineMenu } from 'react-icons/ai';
import { FaGithub, FaLinkedinIn } from 'react-icons/fa';
import { BsFillPersonLinesFill } from 'react-icons/bs';
import {AiOutlineHome} from 'react-icons/ai'
import {RxPerson} from 'react-icons/rx'
// import { useRouter } from 'next/router';

const Navbar = () => {
  const [nav, setNav] = useState(false);
  const [shadow, setShadow] = useState(false);
  const [navBg, setNavBg] = useState('#fff');
  const [linkColor, setLinkColor] = useState('#1f2937');
  const [position, setPosition] = useState('fixed')


  const handleNav = () => {
    setNav(!nav);
  };

  useEffect(() => {
    const handleShadow = () => {
      if (window.scrollY >= 90) {
        setShadow(true);
      } else {
        setShadow(false);
      }
    };
    window.addEventListener('scroll', handleShadow);
  }, []);


  return (
    <div
      style={{ backgroundColor: `${navBg}` }}
      className={
        shadow
          ? 'fixed w-full h-20 shadow-xl z-[100] ease-in-out duration-300'
          : 'fixed w-full h-20 z-[100]'
      }
    >
      <div className='flex justify-between items-center w-full h-full px-2 2xl:px-16'>
        <Link href='/'>
          <a>
          </a>
        </Link>
        <div>
          <ul style={{ color: `${linkColor}` }} className='hidden md:flex'>
            <li className='ml-10 text-m uppercase hover:border-b'>
              <div className="flex items-stretch">
                <div className='pt-1 pr-2 scale-110'>
                  <AiOutlineHome/>
                </div>
                <Link href='/'>Home</Link>
              </div>
            </li>

            <li className='ml-10 text-m uppercase hover:border-b'>
              <div className="flex items-stretch">
                <div className='pt-1 pr-2 scale-110'>
                   <RxPerson/>
                </div>
              <Link href='/#about'>About</Link>
              </div>
            </li>

            <li className='ml-10 text-m uppercase hover:border-b'>
            <div className="flex items-stretch">
            <div className='pt-1 pr-2 scale-110'>
              <AiOutlineMail/>
              </div>
              <Link href='/#contact'>Contact</Link>
              </div>

            </li>
          </ul>
          {/* Hamburger Icon */}
          <div
            style={{ color: `${linkColor}` }}
            onClick={handleNav}
            className='md:hidden'
          >
            <AiOutlineMenu size={25} />
          </div>
        </div>
      </div>

      {/* Mobile Menu */}
      {/* Overlay */}
      <div onClick={handleNav}
        className={
          nav ? 'md:hidden fixed left-0 top-0 w-full h-screen bg-black/70' : ''
        }
      >


        {/* Side Drawer Menu */}
        <div 
          className={
            nav
              ? ' fixed left-0 top-0 w-[75%] sm:w-[60%] md:w-[45%] h-screen bg-[#ecf0f3] p-10 ease-in duration-500'
              : 'fixed left-[-100%] h-screen top-0 p-10 ease-in duration-500'
          }
        >
          <div className='py-4 flex flex-col'>
            <ul className='uppercase'>
              <Link href='/'>
                <li onClick={() => setNav(false)} className='py-4 text-m'>
                  <div className="flex items-stretch">
                    <div className='pt-1 pr-2 scale-110'>
                      <AiOutlineHome/>
                    </div>
                  Home
                  </div>
                </li>
              </Link>
              <Link href='/#about'>
                <li onClick={() => setNav(false)} className='py-4 text-m'>
                <div className="flex items-stretch">
                    <div className='pt-1 pr-2 scale-110'>
                      <RxPerson/>
                    </div>
                  About
                  </div>
                </li>
              </Link>
              <Link href='/#contact'>
                <li onClick={() => setNav(false)} className='py-4 text-m'>
                  <div className="flex items-stretch">
                    <div className='pt-1 pr-2 scale-110'>
                      <AiOutlineMail/>
                    </div>
                  Contact
                  </div>
                </li>
              </Link>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
