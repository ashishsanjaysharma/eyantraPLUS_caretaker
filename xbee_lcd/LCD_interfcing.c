/********************************************************************************
Team Id: eYRC+ #75
* Author List: Dhiraj Gehlot, Amit Yadav, Ashsish Sharma, Rohit Ramakrishnan
* Filename: LCD_interfacing
* Theme: 		eYRC-Plus - "Caretaker Robot"
* Functions: 		N/A, Headers included for XBEE,LCD, Position encoder,buzzer and velocity setting.
* Global Variables:	*Direction of turn string sent from master: dir.
					*conversion from string to ascii:hun,ten,one,angle.
					*Flag for turning on LED: onr1,ong1,onb1,onr2,ong2,onb2.
					
*Description: Code for Caretaker robot. Firebird V is configured in slave mode.
			  Two LEDs to indicate picked provisions, connected to PORTJ PJ0-7.	

**************************************************************************************
Note: 
 
 1. Make sure that in the configuration options following settings are 
 	done for proper operation of the code

 	Microcontroller: atmega2560
 	Frequency: 14745600
 	Optimization: -O0 (For more information read section: Selecting proper optimization 
 					options below figure 2.22 in the Software Manual)

 2. Buzzer is connected to PC3. Hence to operate buzzer without interfering with the LCD, 
 	buzzer should be turned on or off only using buzzer function 

*********************************************************************************/


#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "lcd.h"
#include "xbee.h"
#include "pos_encoder.h"
#include <math.h>
#include "buzzer.h"
#include "velocity.h"


//Function to Initialize PORTS
void port_init()
{
	lcd_port_config();
	motion_pin_config(); //robot motion pins config
 	left_encoder_pin_config(); //left encoder pin config
 	right_encoder_pin_config(); //right encoder pin config
	buzzer_pin_config();
	
}


void init_devices (void)
{
 cli(); //Clears the global interrupts
 port_init();
 uart0_init(); //Initailize UART0 for serial communiaction
 uart2_init(); //Initailize UART1 for serial communiaction
 port_init();  //Initializes all the ports for motion, buzzer, LCD etc.
 left_position_encoder_interrupt_init();
 right_position_encoder_interrupt_init();
 timer5_init();
 sei();   //Enables the global interrupts
}		



//=======================Main Function==================================================
int main(void)
{	

	
	init_devices();
//	lcd_set_4bit();
//	lcd_init();
//	lcd_cursor(1,1);
//	lcd_string("CARETAKER KJSCE");
					
	
	int hun,ten,one,angle;
	unsigned char dir;
	int onr1=0,ong1=0,onb1=0,onr2=0,ong2=0,onb2=0;	
	DDRJ = 0xFF;
	
	
	
	while(1)
		{
		
		velocity(245,245);
		_delay_ms(10);
		dir=a[0];		
		hun=a[1]-48;
		ten=a[2]-48;
		one=a[3]-48;

		angle = 100*hun + 10*ten + one;

	



	if(a[0]=='l')
			{
				velocity(225,225);
				left_degrees(angle);
			}
		
		if(a[0]=='r')
			{
				velocity(225,225);
				right_degrees(angle);
			}		
		
		a[0]=0;		//clear array storing Direction for turning string
		i=0;


		switch(data)
		
		{
		
		case 'w':
		{
		stop();
		//_delay_ms(100);
		forward();
			
		break;
		}
	
		case 'a':
		{
		stop();
		//_delay_ms(100);
		left_degrees(90);
		
		data=0;
		break;
		}

		
		case 'd':
		{
		stop();
	//	_delay_ms(100);
		right_degrees(90);
		data=0;
		break;
		}	

		case 's':
		{
		stop();
		break;
		}

		case 'x':
		{
		stop();
	//	_delay_ms(100);
		back();
		break;
		}

		case 't':
		{
			onr1=~onr1;
			data=0;
			break;
		}

		case 'g':
		{
			ong1=~ong1;
			data=0;
			break;
		}

		case 'b':
		{
			onb1=~onb1;
			data=0;
			break;
		}

		case 'y':
		{
			onr2=~onr2;
			data=0;
			break;
		}

		case 'h':
		{
			ong2=~ong2;
			data=0;
			break;
		}

		case 'n':
		{
			onb2=~onb2;
			data=0;
			break;
		}
		

		case 'p': //for buzzer
		{
			stop();
			buzzer_on();
			_delay_ms(3000);
			_delay_ms(2000);
here:		buzzer_off();
			_delay_ms(9000);
			_delay_ms(3000);
			break;
		goto here;
		}
	
							
		default:
		{
		stop();
		break;
		}			



		}
//==========================LED operation=============================
	if(onr1!=0)
		{
			PORTJ = PORTJ|0x01;	// Red1 glow
		}
	else
		{
			PORTJ = PORTJ & 0x0FE;	//red1 off
		}
		
	if(ong1!=0)
		{
			PORTJ = PORTJ|0x03;	//yellow1 glow
		}
	else
		{
			PORTJ = PORTJ & 0xFD;	//yellow1 off
		}
	
	if(onb1!=0)
		{
			PORTJ = PORTJ|0x04; // blue1 on
		}
	else
		{
			PORTJ = PORTJ&0xFB;  // blue1 off
		}

	if(onr2!=0)
		{
			PORTJ = PORTJ|0x08; //red2 on
		}
	else
		{
			PORTJ = PORTJ&0xF7;  //red2 off
		}
	
	if(ong2!=0)
		{
			PORTJ = PORTJ|0x18;  //yellow2 on
		}
	else
		{
			PORTJ = PORTJ&0xEF;  //yellow2 off
 		}

	if(onb2!=0)
		{
			PORTJ = PORTJ|0x20;  //blue2 on
		}
	else
		{
			PORTJ = PORTJ&0xDF;  //blue2 off
		}
	
		}

}


