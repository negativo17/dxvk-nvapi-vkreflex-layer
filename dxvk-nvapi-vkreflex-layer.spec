%global upstream_name dxvk-nvapi

Name:           %{upstream_name}-vkreflex-layer
Version:        0.9.1
Release:        1%{?dist}
Summary:        NVIDIA Reflex Vulkan layer
License:        MIT
URL:            https://github.com/jp7677/%{upstream_name}
ExclusiveArch:  x86_64 aarch64

Source0:        %{url}/archive/v%{version}.tar.gz#/%{upstream_name}-%{version}.tar.gz
Patch0:         dxvk-nvapi-system-headers.patch

BuildRequires:  meson >= 1.0
BuildRequires:  gcc-c++
BuildRequires:  glslang
BuildRequires:  vkroots-devel >= 0^20250716git51c3213-1.fc43
BuildRequires:  vulkan-headers >= 1.4.321

Requires:       vulkan-loader

%description
This Vulkan layer intercepts Vulkan calls made by DXVK-NVAPI, enriches them
with extra data, and forwards to a Vulkan driver that supports
VK_NV_low_latency2 device extension.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
cd layer
%meson -Dabsolute_library_path=false
%meson_build

%install
cd layer
%meson_install

%files
%license LICENSE
%doc README.md
%{_datadir}/vulkan/implicit_layer.d/VkLayer_DXVK_NVAPI_reflex.json
%{_libdir}/libdxvk_nvapi_vkreflex_layer.so

%changelog
* Sat Jan 24 2026 Simone Caronni <negativo17@gmail.com> - 0.9.1-1
- First build.
