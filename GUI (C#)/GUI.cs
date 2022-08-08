using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
using System.Diagnostics;

namespace WindowsFormsApplication2
{
    public partial class Form1 : Form
    {

    public Form1()
        {
            
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

            Process process = new Process();
            process.StartInfo.FileName = "cmd.exe";
            process.StartInfo.CreateNoWindow = false;
            process.StartInfo.RedirectStandardInput = true;
            process.StartInfo.RedirectStandardOutput = true;
            process.StartInfo.UseShellExecute = false;
            process.Start();
            process.StandardInput.WriteLine("cd..");
            process.StandardInput.Flush();
            process.StandardInput.WriteLine("cd..");
            process.StandardInput.Flush();
            process.StandardInput.WriteLine("cd..");
            process.StandardInput.Flush();
            process.StandardInput.WriteLine("cd..");
            process.StandardInput.Flush();
            process.StandardInput.WriteLine("cd Codes");
            process.StandardInput.Flush();
            process.StandardInput.WriteLine("python control_mouse.py --shape-predictor eye-detection-model.dat");
            process.StandardInput.Flush();
            process.StandardInput.Close();
            process.WaitForExit();
            Console.WriteLine(process.StandardOutput.ReadToEnd());
        }

        private void Form1_Load_1(object sender, EventArgs e)
        {
            button1.Text = "Control mouse!";
            button3.Text = "Control robot!";
            button2.Text = "Exit";
            this.Text = "I-EYE";
            label1.Text = "Developer: Abdelrahman Hossam\n\n For contact:\n    Mobile number: +201029409312\n     E-mail: boudyalex321@gmail.com\n\n Brief about me:\n     I am a high school student in Red Sea\n     STEM school that is interested in\n     informatics and artificial intelligence";
            label1.Font = new Font("Calibri", 10, FontStyle.Bold);
            label3.Text = "(1): Click Control mouse button to start";
            label4.Text = "(2): Just look and move your\n eyes to the targeted point";
            label5.Text = "(3): If you want to left click\n just blink with your left eye";
            label6.Text = "(4): If you want to right click\n just blink with your right eye";
            label10.Text= "(1): Click Control robot button to start";
            label9.Text = "(2): Move your eyes up to move forward\n and down to move backward";
            label8.Text = "(3): Move your eyes left to rotate left\n and right to rotate right";
            label7.Text = "Application helps people having absence of arms or having\n paralysis to use the laptop mouse and control a robot\n with only their “EYES”";
            label7.ForeColor = Color.White;
            label7.TextAlign = ContentAlignment.MiddleCenter;
            tabPage1.Text = "Home";
            tabPage3.Text = "Robot controlling help";
            tabPage2.Text = "Mouse controlling help";
            tabPage4.Text = "Contact";
            tabPage5.Text = "Robot movements report";
            this.tabControl1.TabPages.Remove(this.tabPage4);
            this.tabControl1.TabPages.Insert(4, this.tabPage4);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            DialogResult dialogResult = MessageBox.Show("Are you sure you want to quit?", "Bye Bye!", MessageBoxButtons.YesNo);
            if (dialogResult == DialogResult.Yes){
                this.Close();
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Process process = new Process();
            process.StartInfo.FileName = "cmd.exe";
            process.StartInfo.CreateNoWindow = false;
            process.StartInfo.RedirectStandardInput = true;
            process.StartInfo.RedirectStandardOutput = true;
            process.StartInfo.UseShellExecute = false;
            process.Start();
            process.StandardInput.WriteLine("cd..");
            process.StandardInput.Flush();
            process.StandardInput.WriteLine("cd..");
            process.StandardInput.Flush();
            process.StandardInput.WriteLine("cd..");
            process.StandardInput.Flush();
            process.StandardInput.WriteLine("cd..");
            process.StandardInput.Flush();
            process.StandardInput.WriteLine("cd Codes");
            process.StandardInput.Flush();
            process.StandardInput.WriteLine("python control_robot.py --shape-predictor eye-detection-model.dat");
            process.StandardInput.Flush();
            richTextBox1.Text = (process.StandardOutput.ReadToEnd());
            process.StandardInput.Close();
            process.WaitForExit();
        }

    }
}
