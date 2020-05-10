variable "aws_access_key" {
    default = "access_key_here"
}
variable "aws_secret_key" {
   default = " secret_key_here"
}
variable "aws_region" {
  default = "us-west-2"
}
variable "private_key_path" {
  default = "wiht_tf.pem"
}

variable "homepagepath" {
    default = "index.html"
}

provider "aws" {
  access_key="${var.aws_access_key}"
  secret_key="${var.aws_secret_key}"
  region="${var.aws_region}"  
  version="~> 2.7"
}

data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  owners = ["099720109477"]
}

resource "aws_instance" "apache" {
  ami           = "${data.aws_ami.ubuntu.id}"
  instance_type = "t2.micro"
  key_name = "${var.private_key_path}"

    connection {
       user = "ubuntu"
       host = "resource.aws_instance"
       private_key = "${file(var.private_key_path)}"
    }
    provisioner "file" {
    source      = "${var.homepagepath}"
    destination = "/tmp/index.html"
  }
  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install apache2",
      "sudo cp /tmp/index.html /var/www/html/index.html",
      "sudo service apache2 start"
    ]
  }
  tags = {
    Name = "MY-TF-WEB"
  }
}
output "myipaddress" {
  value = "${aws_instance.apache.public_ip}"
}
