using System;
using System.IO;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using AForge.Video;
using AForge.Video.DirectShow;

namespace Video
{
    public partial class Form1 : Form
    {
        private FilterInfoCollection webcam;
        private VideoCaptureDevice cam;

        
        public Form1()
        {
            InitializeComponent();
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            cam = new VideoCaptureDevice(webcam[0].MonikerString);
            cam.NewFrame += new NewFrameEventHandler(cam_NewFrame);
            cam.Start();
            timer1.Enabled = true;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            webcam = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            //Bitmap b = new Bitmap("0002.png");
           // pictureBox2.Image = b;

        }

        private void cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            cam.Stop();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            pictureBox2.Image = pictureBox1.Image;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            FileStream fstream = new FileStream("" + textBox4.Text + ".png", FileMode.Create);
            pictureBox2.Image.Save(fstream, System.Drawing.Imaging.ImageFormat.Png);
            fstream.Close();
            Bitmap b = new Bitmap("foto_001.bmp");
            pictureBox2.Image = b;
        }

        int contador = 0;
        private void pictureBox2_MouseClick(object sender, MouseEventArgs e)
        {
            int pr, pg, pb, qr, qg, qb, mayr, mayg, mayb, menr, meng, menb;
            pr = 200; // ((pictureBox2.Image as Bitmap).GetPixel(e.X, e.Y)).R;
            pg = 71; // ((pictureBox2.Image as Bitmap).GetPixel(e.X, e.Y)).G;
            pb = 59; // ((pictureBox2.Image as Bitmap).GetPixel(e.X, e.Y)).B;
            textBox1.Text = pr.ToString();
            textBox2.Text = pg.ToString();
            textBox3.Text = pb.ToString();
            Graphics g = pictureBox3.CreateGraphics();
            Pen pluma = new Pen(Color.Blue, 1);
            contador = 0;
            for (int ren = 0; ren < 240; ren++)
            {
                for (int col = 0; col < 360; col++)
                {
                    qr = ((pictureBox2.Image as Bitmap).GetPixel(col, ren)).R;
                    qg = ((pictureBox2.Image as Bitmap).GetPixel(col, ren)).G;
                    qb = ((pictureBox2.Image as Bitmap).GetPixel(col, ren)).B;
                    menr = pr - 45;
                    meng = pg - 45;
                    menb = pb - 45;
                    mayr = pr + 45;
                    mayg = pg + 45;
                    mayb = pb + 45;
                    if ((qr >= menr && qr <= mayr) && (qg >= meng && qg <= mayg) && (qb >= menb && qb <= mayb))
                    {
                        g.DrawRectangle(pluma, col, ren, 1, 1);
                        contador++;
                    }
                }
            }
            //MessageBox.Show("Fin");
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {
            button3_Click(sender, e);
            pictureBox2_MouseClick(sender, null);
            if (contador > 4000)
                textBox4.Text = "presente";
            //MessageBox.Show("objeto identificado!\ncontador = " + contador.ToString());
            else textBox4.Text = ""; //MessageBox.Show("El objeto no esta presente!\ncontador = " + contador.ToString());
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            button5_Click(sender, e);
        }
    }
}
