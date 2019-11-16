using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace manipulator3
{
    public class Manipulator
    {
        public string Manipulate(string x)
        {
            var a = "";
            string[] u;
            for (var i = x.Count(z => z == '\n') + 1; i > 0; i++)
            {
                u = x.Split(new[] { '\n' })[i-1].Split(
                    ':')[0].Substring(0, x.Split(
                        new[] { '\n' })[i].Split(
                        ':')[0].Length - 1).Split(' ');
                if (
                    Convert.ToInt32(u[1].Split(
                        '.')[0].Split(
                        ':')[0])
                    <= (DateTime.Now.ToShortTimeString().Split(
                        ' ')[0].Split(':')[0] == "12" ? (
                        DateTime.Now.ToShortTimeString().Split(
                            ' ')[1] == "AM" ? 12 : 24
                            ) : DateTime.Now.ToShortTimeString(
                                ).Split(
                            ' ')[1] == "AM" ? Convert.ToInt32(
                                DateTime.Now.ToShortTimeString(
                                    ).Split(
                        ' ')[0].Split(':')[0]) : Convert.ToInt32(
                            DateTime.Now.ToShortTimeString(
                                ).Split(
                        ' ')[0].Split(':')[0]) + 12) - 2)
                {
                    break;
                }
                a += x.Split(new[] { '\n' })[i - 1] + '\n';
            }
            a = a.Substring(0, a.Length - 1);
            var b = a.Split('\n').Reverse();
            var c = "";
            foreach (var d in b)
            {
                c += d + '\n';
            }
            return c.Substring(0, a.Length - 1);
        }
    }
}
