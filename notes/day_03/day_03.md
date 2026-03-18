## Day 3 | Virtual Machines Part 1

### What is a Server?

- A **server** is a computer system that provides services, data, or resources to other computers called **clients**.
- Examples:
  - a web server hosts websites
  - a database server stores and manages data
  - a file server stores files for users
    
---

### Physical Machine

- A **physical machine** is the actual hardware computer.
- A physical server runs directly on hardware without sharing it as separate virtual systems.
- It includes:
  - CPU
  - memory (RAM)
  - storage
  - network card
  - motherboard
    
---

### Virtual Machine

- A **virtual machine (VM)** is a software-based computer that runs like a real computer.
- A VM has its own:
  - operating system
  - CPU allocation
  - memory allocation
  - storage
  - network settings
- **Virtualization** helps run multiple isolated systems on one physical server, improving resource usage and reducing cost. 
    
---

### Hypervisor

- A **hypervisor** is the software layer that creates and manages virtual machines.
- It allows multiple VMs to run on one physical machine by sharing hardware resources.
- Main job of a hypervisor:
  - create VMs
  - allocate CPU, memory, and storage
  - isolate VMs from each other
  - manage VM execution
- Examples:
  - VMware ESXi
  - KVM
  - Hyper-V
  - VirtualBox
    
---

### Creating the Virtual Machine

Basic steps to create a VM:

1. install a hypervisor
2. create a new virtual machine
3. assign CPU, RAM, and storage
4. attach an OS image (ISO file)
5. install the operating system
6. start and use the VM

---

### Real-World Example

- Suppose a company has one powerful physical server.
- Instead of using that server for only one purpose, they create multiple VMs on it:
  - **VM 1** → web server
  - **VM 2** → database server
  - **VM 3** → testing server
- This saves:
  - hardware cost
  - space
  - power
  - maintenance effort

---
