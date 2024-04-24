import chisel3._
import circt.stage.ChiselStage
import java.io._

class Echo(steps: Int) extends Module {
  val io = IO(new Bundle {
    val fake_adc  = Input(Vec(steps, UInt(8.W)))
    val fake_dac = Output(Vec(steps, UInt(8.W)))
  })

  val delay = RegInit(VecInit(Seq.fill(steps)(0.U(8.W))))
  delay := io.fake_adc
  io.fake_dac := delay
}

object Hello {
  def main(args: Array[String]) : Unit = {
    val writer = new FileWriter(new File("echo.sv"))
    val sv = ChiselStage.emitSystemVerilog(new Echo(args(0).toInt))
    writer.write(sv)
    writer.close()
  }
}
