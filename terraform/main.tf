# ------------------------------------
# Security Group
# ------------------------------------

resource "aws_security_group" "talentiq_sg" {
  name        = "talentiq-security-group"
  description = "Security Group for TalentIQ AI"

  ingress {
    description = "SSH"

    from_port   = 22
    to_port     = 22
    protocol    = "tcp"

    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Streamlit"

    from_port   = 8501
    to_port     = 8501
    protocol    = "tcp"

    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {

    from_port   = 0
    to_port     = 0
    protocol    = "-1"

    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "TalentIQ-SG"
  }
}

# ------------------------------------
# EC2 Instance
# ------------------------------------

resource "aws_instance" "talentiq_server" {

  ami                    = var.ami_id

  instance_type          = var.instance_type

  key_name               = var.key_name

  vpc_security_group_ids = [
    aws_security_group.talentiq_sg.id
  ]

  tags = {
    Name = "TalentIQ-AI-Server"

    Project = "TalentIQ AI Ranking System"

    Environment = "Development"
  }
}